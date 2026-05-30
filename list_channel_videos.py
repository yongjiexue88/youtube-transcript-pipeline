"""
list_channel_videos.py
----------------------
List all video IDs (and titles) from a YouTube channel using yt-dlp.
Requires yt-dlp: pip install yt-dlp

Usage (CLI):
    python3 list_channel_videos.py <channel_url>
    python3 list_channel_videos.py https://www.youtube.com/@TheValley101/videos
    python3 list_channel_videos.py https://www.youtube.com/@TheValley101/videos --save
    python3 list_channel_videos.py https://www.youtube.com/@TheValley101/videos --format json

Usage (Python):
    from list_channel_videos import list_channel_videos
    videos = list_channel_videos("https://www.youtube.com/@TheValley101/videos")
    for v in videos:
        print(v["id"], v["title"])
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime

# Where channel video lists are saved
CHANNEL_LISTS_DIR = os.path.join(os.path.dirname(__file__), "channel_lists")


def _extract_channel_handle(url: str) -> str:
    """Pull a clean identifier from the channel URL for use in filenames."""
    match = re.search(r"@([\w.-]+)", url)
    if match:
        return match.group(1)
    match = re.search(r"channel/([\w-]+)", url)
    if match:
        return match.group(1)
    return "channel"


def list_channel_videos(channel_url: str) -> list:
    """
    Fetch all video IDs and titles from a YouTube channel.
    Uses yt-dlp to get the flat playlist representation.
    """
    print(f"[→] Fetching video list from: {channel_url}")

    result = subprocess.run(
        [
            sys.executable, "-m", "yt_dlp",
            "--flat-playlist",
            "--print", "%(id)s\t%(title)s",
            "--no-warnings",
            channel_url,
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"[✗] yt-dlp error:\n{result.stderr.strip()}")
        raise RuntimeError("Failed to fetch channel video list.")

    videos = []
    for line in result.stdout.strip().splitlines():
        parts = line.split("\t", 1)
        if len(parts) == 2:
            videos.append({"id": parts[0], "title": parts[1]})
        elif len(parts) == 1 and parts[0]:
            videos.append({"id": parts[0], "title": ""})

    print(f"[✓] Found {len(videos)} videos (via yt-dlp).")
    return videos


def save_video_list(videos: list, channel_url: str, fmt: str = "tsv") -> str:
    """
    Save the video list to a file in channel_lists/.
    """
    os.makedirs(CHANNEL_LISTS_DIR, exist_ok=True)
    handle = _extract_channel_handle(channel_url)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ext = "json" if fmt == "json" else "tsv"
    filename = f"{handle}_{timestamp}.{ext}"
    filepath = os.path.join(CHANNEL_LISTS_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        if fmt == "json":
            json.dump(videos, f, ensure_ascii=False, indent=2)
        else:
            f.write("video_id\ttitle\n")
            for v in videos:
                f.write(f"{v['id']}\t{v['title']}\n")

    print(f"[✓] Saved to → {filepath}")
    return filepath


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="List all video IDs from a YouTube channel."
    )
    parser.add_argument("url", help="YouTube channel URL")
    parser.add_argument(
        "--save", action="store_true",
        help="Save the video list to channel_lists/ folder"
    )
    parser.add_argument(
        "--format", choices=["tsv", "json"], default="tsv",
        help="Output format when saving: tsv (default) or json"
    )
    args = parser.parse_args()

    videos = list_channel_videos(args.url)

    # Always print to stdout
    print()
    print(f"{'#':<5} {'Video ID':<15} Title")
    print("-" * 80)
    for i, v in enumerate(videos, 1):
        print(f"{i:<5} {v['id']:<15} {v['title']}")

    if args.save:
        print()
        save_video_list(videos, args.url, fmt=args.format)
