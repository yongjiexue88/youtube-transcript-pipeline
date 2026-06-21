import sys
from pipeline import fetch_channel_transcripts

channels = [
    {"file": "channel_lists/starterstory_20260620_140756.json", "dir": "transcripts/starterstory"},
    {"file": "channel_lists/saasclub_20260620_200351.json", "dir": "transcripts/saasclub"},
    {"file": "channel_lists/RobWalling_20260620_200500.json", "dir": "transcripts/robwalling"},
    {"file": "channel_lists/Saastr_20260620_200546.json", "dir": "transcripts/saastr"},
    {"file": "channel_lists/MicroConf_20260620_200735.json", "dir": "transcripts/microconf"},
    {"file": "channel_lists/LennysPodcast_20260620_200805.json", "dir": "transcripts/lennyspodcast"},
    {"file": "channel_lists/GregIsenberg_20260620_200831.json", "dir": "transcripts/gregisenberg"},
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
