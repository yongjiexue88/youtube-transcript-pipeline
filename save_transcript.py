"""
save_transcript.py
------------------
Download and save a YouTube transcript to the `transcripts/` folder.
The file is named after the video's title.

Usage (CLI):
    python3 save_transcript.py <video_url_or_id> [language_code]

Usage (Python):
    from save_transcript import save_transcript
    save_transcript("https://www.youtube.com/watch?v=HqsTB0avrh8")
    save_transcript("dQw4w9WgXcQ", languages=["en"])
"""

import os
import re
import sys
from datetime import datetime
from html import unescape

import requests

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
    VideoUnplayable,
    IpBlocked,
    RequestBlocked,
    AgeRestricted,
)

# Folder where all transcripts are saved
TRANSCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "transcripts")

# InnerTube constants (same ones the library uses internally)
_WATCH_URL = "https://www.youtube.com/watch?v={video_id}"
_INNERTUBE_API_URL = "https://www.youtube.com/youtubei/v1/player?key={api_key}"
_INNERTUBE_CONTEXT = {"client": {"clientName": "ANDROID", "clientVersion": "20.10.38"}}


def _extract_video_id(url_or_id: str) -> str:
    """Extract the 11-character video ID from a YouTube URL or return it as-is."""
    patterns = [
        r"(?:v=|youtu\.be/|embed/|shorts/)([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    # Assume it's already a bare video ID
    return url_or_id.strip()


def _sanitize_filename(title: str, max_length: int = 100) -> str:
    """Strip characters that are invalid in filenames and trim to max_length."""
    # Replace filesystem-unsafe characters with underscores
    sanitized = re.sub(r'[\\/:*?"<>|\r\n\t]', "_", title)
    # Collapse multiple spaces/underscores into one
    sanitized = re.sub(r"[\s_]+", "_", sanitized).strip("_")
    return sanitized[:max_length]


def _fetch_video_title(video_id: str) -> str:
    """
    Fetch the video title by hitting YouTube's InnerTube player API.
    Falls back to the video ID if the title cannot be extracted.
    """
    try:
        session = requests.Session()
        session.headers.update({"Accept-Language": "en-US"})

        # Step 1: get the watch page to extract the InnerTube API key
        html = unescape(session.get(_WATCH_URL.format(video_id=video_id)).text)
        match = re.search(r'"INNERTUBE_API_KEY":\s*"([a-zA-Z0-9_-]+)"', html)
        if not match:
            return video_id
        api_key = match.group(1)

        # Step 2: call the InnerTube player endpoint
        response = session.post(
            _INNERTUBE_API_URL.format(api_key=api_key),
            json={"context": _INNERTUBE_CONTEXT, "videoId": video_id},
        )
        data = response.json()
        title = data.get("videoDetails", {}).get("title", "")
        return title if title else video_id
    except Exception:
        return video_id


def save_transcript(
    url_or_id: str,
    languages: list = None,
    output_dir: str = None,
) -> str:
    """
    Fetch a YouTube transcript and save it as a .txt file.

    Parameters
    ----------
    url_or_id : str
        A full YouTube URL (e.g. https://www.youtube.com/watch?v=XYZ)
        or a bare video ID (e.g. XYZ).
    languages : list, optional
        Ordered list of preferred language codes, e.g. ["en", "zh"].
        Defaults to trying all available languages (picks the first one found).
    output_dir : str, optional
        Directory to save the transcript in. Defaults to `transcripts/`.

    Returns
    -------
    str
        Absolute path to the saved transcript file.
    """
    video_id = _extract_video_id(url_or_id)
    save_dir = output_dir or TRANSCRIPTS_DIR
    os.makedirs(save_dir, exist_ok=True)

    api = YouTubeTranscriptApi()

    print(f"[→] Fetching transcript list for: {video_id}")

    try:
        transcript_list = api.list(video_id)
    except TranscriptsDisabled:
        print(f"[✗] Transcripts are disabled for this video ({video_id}).")
        raise
    except VideoUnavailable:
        print(f"[✗] Video unavailable: {video_id}")
        raise
    except VideoUnplayable:
        print(f"[✗] Video is unplayable: {video_id}")
        raise
    except IpBlocked:
        print(f"[✗] Your IP is blocked by YouTube. Try using a proxy.")
        raise
    except RequestBlocked:
        print(f"[✗] Request blocked by YouTube (bot detection). Try using a proxy.")
        raise
    except AgeRestricted:
        print(f"[✗] Video is age-restricted: {video_id}")
        raise

    # Print available transcripts
    available = list(transcript_list)
    print(f"[i] Available transcripts ({len(available)}):")
    for t in available:
        kind = "auto-generated" if t.is_generated else "manual"
        print(f"    [{t.language_code}] {t.language} ({kind})")

    # Pick transcript by preferred language, or fallback to first available
    transcript_obj = None
    if languages:
        try:
            transcript_obj = transcript_list.find_transcript(languages)
        except NoTranscriptFound:
            print(f"[!] No transcript found for languages {languages}, falling back to first available.")

    if transcript_obj is None:
        transcript_obj = available[0]

    print(f"[→] Fetching [{transcript_obj.language_code}] {transcript_obj.language} ...")
    fetched = transcript_obj.fetch()

    # Fetch the video title first (used in both header and filename)
    print(f"[→] Fetching video title ...")
    title = _fetch_video_title(video_id)
    print(f"[i] Title: {title}")

    # Build file content
    lines = []
    lines.append(f"Title     : {title}")
    lines.append(f"Video ID  : {video_id}")
    lines.append(f"URL       : https://www.youtube.com/watch?v={video_id}")
    lines.append(f"Language  : {fetched.language} ({fetched.language_code})")
    lines.append(f"Generated : {'Yes (auto-generated)' if fetched.is_generated else 'No (manually created)'}")
    lines.append(f"Snippets  : {len(fetched)}")
    lines.append(f"Saved at  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 60)
    lines.append("")
    for snippet in fetched:
        mins = int(snippet.start // 60)
        secs = snippet.start % 60
        lines.append(f"[{mins:02d}:{secs:05.2f}]  {snippet.text}")
    content = "\n".join(lines)

    # Build filename: TITLE_LANGCODE.txt
    safe_title = _sanitize_filename(title)
    filename = f"{safe_title}_{fetched.language_code}.txt"
    filepath = os.path.join(save_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[✓] Transcript saved → {filepath}")
    return filepath


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 save_transcript.py <youtube_url_or_video_id> [lang1 lang2 ...]")
        print("Examples:")
        print("  python3 save_transcript.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print("  python3 save_transcript.py dQw4w9WgXcQ en")
        print("  python3 save_transcript.py HqsTB0avrh8 zh")
        sys.exit(1)

    url_or_id = sys.argv[1]
    langs = sys.argv[2:] if len(sys.argv) > 2 else None

    save_transcript(url_or_id, languages=langs)
