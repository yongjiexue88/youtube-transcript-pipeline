import sys
from pipeline import fetch_channel_transcripts

channels = [
    {"file": "channel_lists/starterstory_20260626_125828.json", "dir": "transcripts/starterstory"},
    {"file": "channel_lists/saasclub_20260620_200351.json", "dir": "transcripts/saasclub"},
    {"file": "channel_lists/RobWalling_20260626_125207.json", "dir": "transcripts/robwalling"},
    {"file": "channel_lists/Saastr_20260626_125349.json", "dir": "transcripts/saastr"},
    {"file": "channel_lists/MicroConf_20260626_125110.json", "dir": "transcripts/microconf"},
    {"file": "channel_lists/LennysPodcast_20260626_125107.json", "dir": "transcripts/lennyspodcast"},
    {"file": "channel_lists/GregIsenberg_20260626_125046.json", "dir": "transcripts/gregisenberg"},
]

for chan in channels:
    print(f"\n>>> Starting download for {chan['file']} -> {chan['dir']}")
    try:
        fetch_channel_transcripts(
            channel_url_or_file=chan["file"],
            languages=["en"],
            delay=6.0,
            output_dir=chan["dir"],
            webshare_username="",
            webshare_password="",
        )
    except Exception as e:
        print(f"Error downloading {chan['file']}: {e}")
