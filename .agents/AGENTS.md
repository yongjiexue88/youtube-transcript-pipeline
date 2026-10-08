# Project Customization: Channel Transcript Download Flow

When the user provides a channel name in the format `transcripts/{channel_name}/` (for example, `transcripts/mikelaoli/`), you must follow this automated workflow:

## Workflow Steps:

1. **Resolve Channel URL & Fetch Video List**:
   - Determine the YouTube channel handle (e.g., `@mikelaoli` or `@channel_name` from the suffix).
   - Construct the channel videos URL: `https://www.youtube.com/@{channel_name}/videos`.
   - Run the video listing script to save the list:
     ```bash
     python3 list_channel_videos.py https://www.youtube.com/@{channel_name}/videos --save --format json
     ```
   - Locate the generated JSON file under the `channel_lists/` directory (e.g., `channel_lists/{channel_name}_YYYYMMDD_HHMMSS.json`).

2. **Query for Video Count**:
   - Read the saved video list to find the total count of videos found.
   - **Stop and ask the user explicitly** how many videos they want to download (e.g., all 70, or a specific limit like 10, 20, etc.).

3. **Execute Downloader**:
   - Once the user specifies the count (let's say `N`), execute the download pipeline in the background using the unbuffered `-u` flag for real-time logs, the 5-second delay, and IP rotation:
     ```bash
     python3 -u pipeline.py channel channel_lists/{channel_name}_timestamp.json \
       --output-dir transcripts/{channel_name} \
       --delay 5 \
       --max-videos N
     ```
     *(Note: The script automatically loads Webshare rotating proxy credentials from `.env` to enable IP rotation).*
   - Provide the background task ID to the user and stream the real-time progress by showing `tail` updates from the log file.
