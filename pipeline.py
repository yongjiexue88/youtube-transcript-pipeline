"""
pipeline.py
-----------
YouTube Transcript Pipeline — two top-level functions:

  1. fetch_video_transcript(url)
     Download and save the transcript for a single YouTube video.

  2. fetch_channel_transcripts(channel_url)
     Loop through every video in a channel and save each transcript.

All transcripts are saved to the `transcripts/` folder, named after the
video title.

Usage (CLI):
    # Single video
    python3 pipeline.py video 'https://www.youtube.com/watch?v=HqsTB0avrh8'

    # Whole channel
    python3 pipeline.py channel 'https://www.youtube.com/@TheValley101/videos'

    # Channel with specific language preference
    python3 pipeline.py channel 'https://www.youtube.com/@TheValley101/videos' --languages zh en

Usage (Python):
    from pipeline import fetch_video_transcript, fetch_channel_transcripts

    fetch_video_transcript("https://www.youtube.com/watch?v=HqsTB0avrh8")
    fetch_channel_transcripts("https://www.youtube.com/@TheValley101/videos")
"""

from __future__ import annotations  # enables str | None on Python 3.9

import argparse
import json
import os
import random
import re
import sys
import time

from save_transcript import save_transcript, TRANSCRIPTS_DIR
from list_channel_videos import list_channel_videos, save_video_list

from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
    VideoUnplayable,
    IpBlocked,
    RequestBlocked,
    AgeRestricted,
)

# Errors we skip silently (no transcript available for this video)
_SKIPPABLE_ERRORS = (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
    VideoUnplayable,
    AgeRestricted,
)

# Errors that mean we're blocked — stop the whole run
_FATAL_ERRORS = (IpBlocked, RequestBlocked)


# Helper functions for the pipeline
def str2bool(v: str | bool) -> bool:
    """Parse boolean strings for argparse."""
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


def get_downloaded_video_ids(directory: str) -> set[str]:
    """Scan the directory for existing transcripts and extract video IDs from their headers."""
    downloaded = set()
    if not os.path.isdir(directory):
        return downloaded
    for filename in os.listdir(directory):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                # Read first few lines (Video ID is usually on line 2)
                for _ in range(5):
                    line = f.readline()
                    if not line:
                        break
                    match = re.match(r"^Video ID\s*:\s*([a-zA-Z0-9_-]{11})", line)
                    if match:
                        downloaded.add(match.group(1))
                        break
        except Exception:
            pass
    return downloaded


def load_video_list(filepath: str) -> list[dict]:
    """Load a list of videos from a TSV or JSON file."""
    if filepath.endswith(".json"):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Assume TSV
        videos = []
        with open(filepath, "r", encoding="utf-8") as f:
            header = f.readline().strip().split("\t")
            # Expected header: video_id \t title
            for line in f:
                parts = line.strip().split("\t", 1)
                if len(parts) == 2:
                    videos.append({"id": parts[0], "title": parts[1]})
                elif len(parts) == 1 and parts[0]:
                    videos.append({"id": parts[0], "title": ""})
        return videos


def is_blocking_error(exception: Exception) -> bool:
    """Check if the exception is due to IP blocking, rate limiting (429), or service unavailability (503)."""
    if isinstance(exception, _FATAL_ERRORS):
        return True
    err_str = str(exception)
    if "429" in err_str or "503" in err_str:
        return True
    cause = getattr(exception, "cause", "")
    if cause and ("429" in cause or "503" in cause):
        return True
    return False


def _get_proxy_env_defaults() -> dict[str, str | None]:
    """Load proxy variables from .env file or environment variables."""
    res = {
        "webshare_username": os.environ.get("WEBSHARE_USERNAME"),
        "webshare_password": os.environ.get("WEBSHARE_PASSWORD"),
        "http_proxy": os.environ.get("HTTP_PROXY"),
        "https_proxy": os.environ.get("HTTPS_PROXY"),
    }
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        parts = line.split("=", 1)
                        if len(parts) == 2:
                            key = parts[0].strip()
                            val = parts[1].strip().strip('"').strip("'")
                            if key == "WEBSHARE_USERNAME":
                                res["webshare_username"] = val
                            elif key == "WEBSHARE_PASSWORD":
                                res["webshare_password"] = val
                            elif key == "HTTP_PROXY":
                                res["http_proxy"] = val
                            elif key == "HTTPS_PROXY":
                                res["https_proxy"] = val
        except Exception:
            pass
    return res



# ─────────────────────────────────────────────
# Function 1: Single video
# ─────────────────────────────────────────────

def fetch_video_transcript(
    url_or_id: str,
    languages: list = None,
    output_dir: str = None,
    webshare_username: str = None,
    webshare_password: str = None,
    http_proxy: str = None,
    https_proxy: str = None,
) -> str | None:
    """
    Download and save the transcript for a single YouTube video.

    Parameters
    ----------
    url_or_id : str
        Full YouTube URL or bare video ID.
    languages : list, optional
        Preferred language codes in priority order, e.g. ["zh", "en"].
        Defaults to the first available language.
    webshare_username : str, optional
        Username for Webshare proxy.
    webshare_password : str, optional
        Password for Webshare proxy.
    http_proxy : str, optional
        Generic HTTP proxy URL.
    https_proxy : str, optional
        Generic HTTPS proxy URL.

    Returns
    -------
    str  Path to the saved transcript file, or None if unavailable.
    """
    print("=" * 60)
    print(f"  VIDEO  : {url_or_id}")
    print("=" * 60)
    try:
        path = save_transcript(
            url_or_id,
            languages=languages,
            output_dir=output_dir,
            webshare_username=webshare_username,
            webshare_password=webshare_password,
            http_proxy=http_proxy,
            https_proxy=https_proxy,
        )
        print()
        return path
    except _SKIPPABLE_ERRORS as e:
        print(f"[!] Skipped — no transcript available: {type(e).__name__}")
        print()
        return None
    except _FATAL_ERRORS:
        print("[✗] Blocked by YouTube. Try again later or use a proxy.")
        print()
        return None
    except Exception as e:
        if is_blocking_error(e):
            print(f"[✗] Blocked/rate-limited by YouTube after retries: {type(e).__name__}")
            print()
            return None
        raise


# ─────────────────────────────────────────────
# Function 2: Whole channel
# ─────────────────────────────────────────────

def fetch_channel_transcripts(
    channel_url_or_file: str,
    languages: list = None,
    delay: float = 10.0,
    max_videos: int | None = None,
    resume: bool = True,
    stop_on_block: bool = True,
    random_delay: bool = True,
    output_dir: str = None,
    webshare_username: str = None,
    webshare_password: str = None,
    http_proxy: str = None,
    https_proxy: str = None,
) -> dict:
    """
    Loop through every video in a YouTube channel or a local video list file
    and save each transcript.

    Parameters
    ----------
    channel_url_or_file : str
        Any YouTube channel URL, or a local path to a saved TSV/JSON video list.
    languages : list, optional
        Preferred language codes in priority order, e.g. ["zh", "en"].
        Defaults to the first available language for each video.
    delay : float, optional
        Seconds to wait between requests (default 10.0) to avoid rate-limiting.
    max_videos : int, optional
        Maximum number of videos to crawl.
    resume : bool, optional
        Whether to skip already downloaded transcripts (default True).
    stop_on_block : bool, optional
        Whether to stop cleanly when blocked by YouTube (default True).
    random_delay : bool, optional
        Whether to randomize delay (default True) to avoid detection.
    webshare_username : str, optional
        Username for Webshare proxy.
    webshare_password : str, optional
        Password for Webshare proxy.
    http_proxy : str, optional
        Generic HTTP proxy URL.
    https_proxy : str, optional
        Generic HTTPS proxy URL.

    Returns
    -------
    dict  Summary with keys: "saved", "skipped", "failed", "paths"
    """
    if os.path.exists(channel_url_or_file):
        print(f"[→] Loading video list from file: {channel_url_or_file}")
        videos = load_video_list(channel_url_or_file)
    else:
        videos = list_channel_videos(channel_url_or_file)
        # Crawl once, save video list, cache everything
        try:
            saved_list_path = save_video_list(videos, channel_url_or_file, fmt="json")
            print(f"[✓] Cached video list at: {saved_list_path}")
        except Exception as e:
            print(f"[!] Warning: failed to cache video list: {e}")

    if max_videos is not None:
        print(f"[i] Limiting run to first {max_videos} videos.")
        videos = videos[:max_videos]

    total = len(videos)
    saved, skipped, failed = [], [], []

    downloaded_ids = set()
    target_dir = output_dir if output_dir else TRANSCRIPTS_DIR
    if resume:
        downloaded_ids = get_downloaded_video_ids(target_dir)
        print(f"[i] Resume enabled: Found {len(downloaded_ids)} already-downloaded transcripts.")

    print()
    print("=" * 60)
    print(f"  CHANNEL TRANSCRIPT PIPELINE")
    print(f"  Source  : {channel_url_or_file}")
    print(f"  Videos  : {total}")
    print(f"  Languages: {languages or 'auto (first available)'}")
    print(f"  Base Delay: {delay}s (Randomized: {random_delay})")
    print(f"  Resume  : {resume}")
    print(f"  Stop on Block: {stop_on_block}")
    if webshare_username or http_proxy or https_proxy:
        print("  Proxy   : Enabled")
    print("=" * 60)
    print()

    for i, video in enumerate(videos, 1):
        video_id = video["id"]
        title    = video["title"]
        url      = f"https://www.youtube.com/watch?v={video_id}"

        # If resume is enabled, check if we already have it
        if resume and video_id in downloaded_ids:
            print(f"[{i}/{total}] {title[:60]}")
            print(f"  [i] Skipped — Already downloaded (resume)")
            skipped.append({"id": video_id, "title": title, "reason": "AlreadyDownloaded"})
            continue

        print(f"[{i}/{total}] {title[:60]}")

        try:
            path = save_transcript(
                url,
                languages=languages,
                output_dir=target_dir,
                webshare_username=webshare_username,
                webshare_password=webshare_password,
                http_proxy=http_proxy,
                https_proxy=https_proxy,
            )
            saved.append({"id": video_id, "title": title, "path": path})

        except _SKIPPABLE_ERRORS as e:
            reason = type(e).__name__
            print(f"  [!] Skipped — {reason}")
            skipped.append({"id": video_id, "title": title, "reason": reason})

        except Exception as e:
            if stop_on_block and is_blocking_error(e):
                print(f"  [✗] FATAL/BLOCK: {type(e).__name__}: {e}")
                print(f"  [i] stop-on-block is True. Stopping cleanly after {i-1} videos.")
                failed.append({"id": video_id, "title": title, "reason": f"Blocked ({type(e).__name__})"})
                break
            
            # Treat other exceptions or fatal errors when stop_on_block is False
            if isinstance(e, _FATAL_ERRORS):
                print(f"  [✗] FATAL: Blocked by YouTube after {i} videos.")
                failed.append({"id": video_id, "title": title, "reason": type(e).__name__})
                if stop_on_block:
                    break
            else:
                print(f"  [✗] Unexpected error: {e}")
                failed.append({"id": video_id, "title": title, "reason": str(e)})

        # Polite delay between requests
        if i < total:
            if random_delay:
                actual_delay = random.uniform(0.8 * delay, 1.6 * delay)
            else:
                actual_delay = delay
            
            if actual_delay > 0.5:
                print(f"  [i] Waiting {actual_delay:.2f} seconds...")
            time.sleep(actual_delay)

    # ── Summary ─────────────────────────────
    print()
    print("=" * 60)
    print(f"  DONE — {total} videos processed")
    print(f"  ✓ Saved   : {len(saved)}")
    print(f"  ⚠ Skipped : {len(skipped)}")
    print(f"  ✗ Failed  : {len(failed)}")
    print("=" * 60)

    if skipped:
        print("\nSkipped videos:")
        for v in skipped:
            print(f"  [{v['id']}] {v['title'][:50]}  → {v['reason']}")

    if failed:
        print("\nFailed videos:")
        for v in failed:
            print(f"  [{v['id']}] {v['title'][:50]}  → {v['reason']}")

    return {"saved": saved, "skipped": skipped, "failed": failed}


# ─────────────────────────────────────────────
# CLI entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="YouTube Transcript Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download transcript for one video
  python3 pipeline.py video 'https://www.youtube.com/watch?v=HqsTB0avrh8'

  # Download transcript in a specific language
  python3 pipeline.py video 'https://www.youtube.com/watch?v=HqsTB0avrh8' --languages zh

  # Download all transcripts from a channel
  python3 pipeline.py channel 'https://www.youtube.com/@TheValley101/videos'

  # Channel with language preference and slower rate
  python3 pipeline.py channel 'https://www.youtube.com/@TheValley101/videos' --languages zh en --delay 2
        """,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ── `video` subcommand ──────────────────
    video_parser = subparsers.add_parser("video", help="Fetch transcript for a single video")
    video_parser.add_argument("url", help="YouTube video URL or video ID")
    video_parser.add_argument(
        "--languages", nargs="+", default=None,
        metavar="LANG",
        help="Preferred language codes in priority order (e.g. --languages zh en)"
    )
    
    # ── `channel` subcommand ────────────────
    channel_parser = subparsers.add_parser("channel", help="Fetch transcripts for all videos in a channel")
    channel_parser.add_argument("url", help="YouTube channel URL or path to local video list file")
    channel_parser.add_argument(
        "--languages", nargs="+", default=None,
        metavar="LANG",
        help="Preferred language codes in priority order (e.g. --languages zh en)"
    )
    channel_parser.add_argument(
        "--delay", type=float, default=10.0,
        help="Seconds to wait between videos (default: 10.0)"
    )
    channel_parser.add_argument(
        "--max-videos", type=int, default=None,
        help="Maximum number of videos to download transcripts for (optional)"
    )
    channel_parser.add_argument(
        "--resume", type=str2bool, nargs="?", const=True, default=True,
        help="Skip already-downloaded transcripts (default: True)"
    )
    channel_parser.add_argument(
        "--stop-on-block", type=str2bool, nargs="?", const=True, default=True,
        help="Stop cleanly if blocked by YouTube (default: True)"
    )
    channel_parser.add_argument(
        "--random-delay", type=str2bool, nargs="?", const=True, default=True,
        help="Randomize delay between 0.8*delay and 1.6*delay (default: True)"
    )

    # ── Proxy Arguments ─────────────────────
    proxy_defaults = _get_proxy_env_defaults()
    
    for parser_obj in (video_parser, channel_parser):
        parser_obj.add_argument(
            "--output-dir", default=None,
            help="Directory to save transcripts (default: transcripts/)"
        )
        parser_obj.add_argument(
            "--webshare-username", default=proxy_defaults["webshare_username"],
            help="Username for Webshare rotating residential proxy"
        )
        parser_obj.add_argument(
            "--webshare-password", default=proxy_defaults["webshare_password"],
            help="Password for Webshare rotating residential proxy"
        )
        parser_obj.add_argument(
            "--http-proxy", default=proxy_defaults["http_proxy"],
            help="Generic HTTP proxy URL"
        )
        parser_obj.add_argument(
            "--https-proxy", default=proxy_defaults["https_proxy"],
            help="Generic HTTPS proxy URL"
        )

    args = parser.parse_args()

    if args.command == "video":
        fetch_video_transcript(
            args.url,
            languages=args.languages,
            output_dir=args.output_dir,
            webshare_username=args.webshare_username,
            webshare_password=args.webshare_password,
            http_proxy=args.http_proxy,
            https_proxy=args.https_proxy,
        )

    elif args.command == "channel":
        fetch_channel_transcripts(
            args.url,
            languages=args.languages,
            delay=args.delay,
            max_videos=args.max_videos,
            resume=args.resume,
            stop_on_block=args.stop_on_block,
            random_delay=args.random_delay,
            output_dir=args.output_dir,
            webshare_username=args.webshare_username,
            webshare_password=args.webshare_password,
            http_proxy=args.http_proxy,
            https_proxy=args.https_proxy,
        )
