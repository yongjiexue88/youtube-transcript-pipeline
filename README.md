<h1 align="center">
  ✨ YouTube Transcript API ✨
</h1>

<p align="center">
  <a href="https://github.com/sponsors/jdepoix">
    <img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86" alt="Sponsor">
  </a>
  <a href="https://www.paypal.com/donate/?hosted_button_id=9W5ZHV22FD63G">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="Donate">
  </a>
  <a href="https://github.com/jdepoix/youtube-transcript-api/actions">
    <img src="https://github.com/jdepoix/youtube-transcript-api/actions/workflows/ci.yml/badge.svg?branch=master" alt="Build Status">
  </a>
  <a href="https://coveralls.io/github/jdepoix/youtube-transcript-api?branch=master">
    <img src="https://coveralls.io/repos/github/jdepoix/youtube-transcript-api/badge.svg?branch=master" alt="Coverage Status">
  </a>
  <a href="http://opensource.org/licenses/MIT">
    <img src="http://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat" alt="MIT license">
  </a>
  <a href="https://pypi.org/project/youtube-transcript-api/">
    <img src="https://img.shields.io/pypi/v/youtube-transcript-api.svg" alt="Current Version">
  </a>
  <a href="https://pypi.org/project/youtube-transcript-api/">
    <img src="https://img.shields.io/pypi/pyversions/youtube-transcript-api.svg" alt="Supported Python Versions">
  </a>
</p>

<p align="center">
  This is a python API which allows you to retrieve the transcript/subtitles for a given YouTube video. It also works for automatically generated subtitles, supports translating subtitles and it does not require a headless browser, like other selenium based solutions do!
</p>

<br />

<p align="center">
 <b>If you feel more comfortable using a hosted solution, you can use the services of any of our amazing sponsors:</b>
</p>

<p align="center">
  <a href="https://serpapi.com/youtube-video-transcript">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/87d28ff2-c478-4fbf-b27e-9bced1271603">
      <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/43f6fa61-9ee4-442b-9e11-6d2b6d3116ee">
      <img alt="SerpApi" src="https://github.com/user-attachments/assets/43f6fa61-9ee4-442b-9e11-6d2b6d3116ee" height="100px" style="vertical-align: middle;">
    </picture>
  </a>
</p>

<p align="center">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://transcriptapi.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://anacreon.ai/downloads/transcriptapi-logo-color.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://anacreon.ai/downloads/transcriptapi-logo-black.svg">
      <img alt="TranscriptAPI.com" src="https://anacreon.ai/downloads/transcriptapi-logo-black.svg" height="50px" style="vertical-align: middle;">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://supadata.ai/youtube-transcript-api?ref=ytt-api">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://supadata.ai/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://supadata.ai/logo-light.svg">
      <img alt="supadata" src="https://supadata.ai/logo-light.svg" height="25px">
    </picture>
  </a>
  &nbsp;&nbsp;
  <a href="https://www.dumplingai.com/endpoints/get-youtube-transcript?via=ytt-api">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://www.dumplingai.com/logos/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://www.dumplingai.com/logos/logo-light.svg">
      <img alt="Dumpling AI" src="https://www.dumplingai.com/logos/logo-light.svg" height="25px" style="vertical-align: middle;">
    </picture>
  </a>
</p>

<br />

<p align="center">
  Maintenance of this project is made possible by all the <a href="https://github.com/jdepoix/youtube-transcript-api/graphs/contributors">contributors</a> and <a href="https://github.com/sponsors/jdepoix">sponsors</a>. If you'd like to sponsor this project <a href="https://github.com/sponsors/jdepoix">click here</a>. 💖
</p>

## YouTube Transcript Pipeline CLI Wrapper (`pipeline.py`)

This repository contains a CLI wrapper, `pipeline.py`, designed for crawling entire channels safely and robustly without triggering YouTube's rate limiting blocks.

### Quick Start

1. Fetch transcripts for a single video:
   ```bash
   python3 pipeline.py video 'https://www.youtube.com/watch?v=HqsTB0avrh8'
   ```

2. Fetch all transcripts from a channel:
   ```bash
   python3 pipeline.py channel 'https://www.youtube.com/@TheValley101/videos'
   ```

### Two-Step Crawling Workflow (Recommended)

For larger channels, it is recommended to retrieve the list of video IDs first, and then run the download pipeline using that list. This prevents querying the channel page repeatedly.

#### Step 1: Save the Video List from a Channel
Fetch and save all uploads from a channel (exclude Shorts by appending `/videos` to the URL) to a TSV file:
```bash
python3 list_channel_videos.py "https://www.youtube.com/@AccurateEnglish/videos" --save
```
This will save a list file under `channel_lists/` (e.g., [channel_lists/AccurateEnglish_20260603_071945.tsv](file:///Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/channel_lists/AccurateEnglish_20260603_071945.tsv)).

#### Step 2: Download Transcripts Using the Saved List
Pass the saved list file directly to `pipeline.py` to start downloading transcripts into your desired directory.

##### Option A: Using Webshare Rotating Residential Proxies (Recommended to avoid IP bans)
YouTube actively blocks IP addresses that make too many requests. Using rotating residential proxies like [Webshare](https://www.webshare.io/?referral_code=w0xno53eb50g) is highly recommended. You can set it up in two ways:

1. **Via Environment Variables (`.env` file - Recommended)**
   Create a `.env` file in the root directory of the project and add your credentials:
   ```env
   WEBSHARE_USERNAME="your_webshare_username"
   WEBSHARE_PASSWORD="your_webshare_password"
   ```
   When these variables are present in the `.env` file, `pipeline.py` automatically loads them. You can then run the pipeline cleanly without specifying credentials in your command:
   ```bash
   python3 -u pipeline.py channel channel_lists/InteractiveEng_20260605_072449.tsv \
     --delay 8 \
     --output-dir transcripts/interactive_english
   ```

2. **Via Command-Line Arguments**
   Alternatively, you can pass the credentials directly into the CLI wrapper commands:
   ```bash
   python3 -u pipeline.py channel channel_lists/InteractiveEng_20260605_072449.tsv \
     --delay 8 \
     --output-dir transcripts/interactive_english \
     --webshare-username "YOUR_USERNAME" \
     --webshare-password "YOUR_PASSWORD"
   ```

##### Option B: Run Without Proxies (Local / Low Volume)
If you are running locally for a small channel/volume and do not require a proxy, you can run the pipeline directly:
```bash
python3 pipeline.py channel channel_lists/AccurateEnglish_20260603_071945.tsv \
  --output-dir transcripts/accurate_english \
  --delay 10
```

### Rate-Limiting & Crawling Rules of Thumb

> [!IMPORTANT]
> **Do not try to "beat" YouTube rate limiting by blasting requests.**
> For crawling channels, the recommended design is:
> 1. **Crawl video list once** and save/cache it locally.
> 2. **Download transcripts slowly** with deliberate, randomized delays.
> 3. **Resume** from where it stopped.
> 4. **Cache everything** so you don't repeat work.

#### Practical Rules of Thumb (for personal/local use):
- **1 video every 3–5 seconds** = Safer (Default)
- **1 video every 1 second** = Risky
- **Parallel requests** = Very risky
- **Cloud server IP** = Much more risky (highly monitored by YouTube)

#### Example Command:
```bash
python3 pipeline.py channel "https://www.youtube.com/@TheValley101/videos" \
  --languages zh en \
  --delay 5
```

### Pipeline Options & Defaults
The `pipeline.py channel` command is pre-configured with safe defaults:
- `--delay 10` (Default base delay of 10.0 seconds).
- `--random-delay true` (Enabled by default; randomizes the sleep interval to `0.8 * delay` to `1.6 * delay`, e.g., 8–16 seconds, to make request patterns natural).
- `--resume true` (Enabled by default; scans the `transcripts/` output folder and automatically skips already-downloaded transcripts).
- `--stop-on-block true` (Enabled by default; stops cleanly on HTTP 429, 503, or IP block exceptions and saves progress instead of throwing hard failures).
- `--max-videos <N>` (Optional limit to fetch transcripts for only up to $N$ videos).
- `--output-dir <path>` (Optional directory to save transcripts; defaults to the `transcripts/` folder).
- `--languages <LANG...>` (Optional ordered list of preferred language codes, e.g., `--languages zh en`).

#### Crawling Once / Resuming from Cached Video List:
When crawling a channel via URL, `pipeline.py` automatically caches the video list in `channel_lists/` in JSON format.
To resume crawling or run safely without querying YouTube for the channel page again, you can pass the cached list file path directly:
```bash
python3 pipeline.py channel channel_lists/TheValley101_20260530_142240.json --delay 5
```

### Reformatting Transcripts to Article/Paragraph Format

By default, transcripts downloaded by `pipeline.py` or `save_transcript.py` are saved in a timestamped format (e.g., `[MM:SS.ms] text`). 

If you want to read transcripts like normal articles or paragraphs, you can use the `reformat_transcripts.py` utility script to convert them into highly readable Markdown (`.md`) files.

#### What Reformatting Does:
1. **Strips Timestamps:** Removes timing tags like `[00:00.03]` from the text.
2. **Groups Paragraphs Flowingly:** Merges lines into readable paragraphs. A new paragraph is started if:
   - There is a pause of more than 3.0 seconds between spoken lines.
   - There is a pause of more than 1.5 seconds combined with sentence-ending punctuation (like `.`, `?`, `!`, or Chinese equivalent punctuation).
3. **Splits Giant Paragraphs:** Auto-generated transcripts (which lack punctuation and normal pauses) can result in massive single blocks of text. The script dynamically splits blocks of text longer than ~100 words (English) or ~200 characters (Chinese) into smaller, logical paragraphs.
4. **Smart Spacing:** Properly joins English words using spaces, and Chinese characters without spaces.
5. **Renames Video ID Titles:** If the video has a title composed of random letters/numbers (such as a YouTube video ID like `0vB4CiIiOYU`), the script extracts the first sentence/meaningful phrase from the content to generate a clean, readable title and renames the file accordingly.
6. **Formats Metadata Table:** Converts metadata headers (Video ID, URL, Language, Saved At, etc.) into a clean, formatted Markdown table at the top of each file.
7. **Converts Files & Cleans Up:** Saves the reformatted transcript as a `.md` file and automatically deletes the original `.txt` file.

#### How to Run:

- **Format/Convert all subdirectories under `transcripts/`:**
  ```bash
  python3 reformat_transcripts.py
  ```

- **Format a specific subdirectory or file:**
  ```bash
  # Format a specific folder
  python3 reformat_transcripts.py transcripts/accurate_english
  
  # Format a specific file (can be a .txt or already converted .md file)
  python3 reformat_transcripts.py transcripts/101/some_file_en.txt
  ```

## Install

Since this repository contains custom pipeline wrappers and local residential proxy enhancements, you should clone this repository and install its dependencies locally using [Poetry](https://python-poetry.org/):

```bash
poetry install
```

To run commands inside the virtual environment created by Poetry, you can prepend them with `poetry run` (for example, `poetry run python3 pipeline.py ...` or `poetry run youtube_transcript_api ...`).

You can either integrate this module [into an existing application](#api) or just use it via a [CLI](#cli).

## API

The easiest way to get a transcript for a given video is to execute:

```python
from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
ytt_api.fetch(video_id)
```

> **Note:** By default, this will try to access the English transcript of the video. If your video has a different 
> language, or you are interested in fetching a transcript in a different language, please read the section below.

> **Note:** Pass in the video ID, NOT the video URL. For a video with the URL `https://www.youtube.com/watch?v=12345` 
> the ID is `12345`.

This will return a `FetchedTranscript` object looking somewhat like this:

```python
FetchedTranscript(
    snippets=[
        FetchedTranscriptSnippet(
            text="Hey there",
            start=0.0,
            duration=1.54,
        ),
        FetchedTranscriptSnippet(
            text="how are you",
            start=1.54,
            duration=4.16,
        ),
        # ...
    ],
    video_id="12345",
    language="English",
    language_code="en",
    is_generated=False,
)
```

This object implements most interfaces of a `List`:

```python
ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id)

# is iterable
for snippet in fetched_transcript:
    print(snippet.text)

# indexable
last_snippet = fetched_transcript[-1]

# provides a length
snippet_count = len(fetched_transcript)
```

If you prefer to handle the raw transcript data you can call `fetched_transcript.to_raw_data()`, which will return 
a list of dictionaries:

```python
[
    {
        'text': 'Hey there',
        'start': 0.0,
        'duration': 1.54
    },
    {
        'text': 'how are you',
        'start': 1.54
        'duration': 4.16
    },
    # ...
]
```
### Retrieve different languages

You can add the `languages` param if you want to make sure the transcripts are retrieved in your desired language 
(it defaults to english).

```python
YouTubeTranscriptApi().fetch(video_id, languages=['de', 'en'])
```

It's a list of language codes in a descending priority. In this example it will first try to fetch the german 
transcript (`'de'`) and then fetch the english transcript (`'en'`) if it fails to do so. If you want to find out 
which languages are available first, [have a look at `list()`](#list-available-transcripts).

If you only want one language, you still need to format the `languages` argument as a list

```python
YouTubeTranscriptApi().fetch(video_id, languages=['de'])
```

### Preserve formatting

You can also add `preserve_formatting=True` if you'd like to keep HTML formatting elements such as `<i>` (italics) 
and `<b>` (bold).

```python
YouTubeTranscriptApi().fetch(video_ids, languages=['de', 'en'], preserve_formatting=True)
```

### List available transcripts

If you want to list all transcripts which are available for a given video you can call:

```python
ytt_api = YouTubeTranscriptApi()
transcript_list = ytt_api.list(video_id)
```

This will return a `TranscriptList` object which is iterable and provides methods to filter the list of transcripts for 
specific languages and types, like:

```python
transcript = transcript_list.find_transcript(['de', 'en'])
```

By default this module always chooses manually created transcripts over automatically created ones, if a transcript in 
the requested language is available both manually created and generated. The `TranscriptList` allows you to bypass this 
default behaviour by searching for specific transcript types:

```python
# filter for manually created transcripts
transcript = transcript_list.find_manually_created_transcript(['de', 'en'])

# or automatically generated ones
transcript = transcript_list.find_generated_transcript(['de', 'en'])
```

The methods `find_generated_transcript`, `find_manually_created_transcript`, `find_transcript` return `Transcript` 
objects. They contain metadata regarding the transcript:

```python
print(
    transcript.video_id,
    transcript.language,
    transcript.language_code,
    # whether it has been manually created or generated by YouTube
    transcript.is_generated,
    # whether this transcript can be translated or not
    transcript.is_translatable,
    # a list of languages the transcript can be translated to
    transcript.translation_languages,
)
```

and provide the method, which allows you to fetch the actual transcript data:

```python
transcript.fetch()
```

This returns a `FetchedTranscript` object, just like `YouTubeTranscriptApi().fetch()` does.

### Translate transcript

YouTube has a feature which allows you to automatically translate subtitles. This module also makes it possible to 
access this feature. To do so `Transcript` objects provide a `translate()` method, which returns a new translated 
`Transcript` object:

```python
transcript = transcript_list.find_transcript(['en'])
translated_transcript = transcript.translate('de')
print(translated_transcript.fetch())
```

### By example
```python
from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()

# retrieve the available transcripts
transcript_list = ytt_api.list('video_id')

# iterate over all available transcripts
for transcript in transcript_list:

    # the Transcript object provides metadata properties
    print(
        transcript.video_id,
        transcript.language,
        transcript.language_code,
        # whether it has been manually created or generated by YouTube
        transcript.is_generated,
        # whether this transcript can be translated or not
        transcript.is_translatable,
        # a list of languages the transcript can be translated to
        transcript.translation_languages,
    )

    # fetch the actual transcript data
    print(transcript.fetch())

    # translating the transcript will return another transcript object
    print(transcript.translate('en').fetch())

# you can also directly filter for the language you are looking for, using the transcript list
transcript = transcript_list.find_transcript(['de', 'en'])  

# or just filter for manually created transcripts  
transcript = transcript_list.find_manually_created_transcript(['de', 'en'])  

# or automatically generated ones  
transcript = transcript_list.find_generated_transcript(['de', 'en'])
```

## Working around IP bans (`RequestBlocked` or `IpBlocked` exception)

Unfortunately, YouTube has started blocking most IPs that are known to belong to cloud providers (like AWS, Google Cloud 
Platform, Azure, etc.), which means you will most likely run into `RequestBlocked` or `IpBlocked` exceptions when 
deploying your code to any cloud solutions. Same can happen to the IP of your self-hosted solution, if you are doing 
too many requests. You can work around these IP bans using proxies. However, since YouTube will ban static proxies 
after extended use, going for rotating residential proxies provide is the most reliable option.

There are different providers that offer rotating residential proxies, but after testing different 
offerings I have found [Webshare](https://www.webshare.io/?referral_code=w0xno53eb50g) to be the most reliable and have 
therefore integrated it into this module, to make setting it up as easy as possible.

### Using [Webshare](https://www.webshare.io/?referral_code=w0xno53eb50g)

Once you have created a [Webshare account](https://www.webshare.io/?referral_code=w0xno53eb50g) and purchased a 
"Residential" proxy package that suits your workload (make sure NOT to purchase "Proxy Server" or 
"Static Residential"!), open the 
[Webshare Proxy Settings](https://dashboard.webshare.io/proxy/settings?referral_code=w0xno53eb50g) to retrieve 
your "Proxy Username" and "Proxy Password". Using this information you can initialize the `YouTubeTranscriptApi` as 
follows:

```python
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig

ytt_api = YouTubeTranscriptApi(
    proxy_config=WebshareProxyConfig(
        proxy_username="<proxy-username>",
        proxy_password="<proxy-password>",
    )
)

# all requests done by ytt_api will now be proxied through Webshare
ytt_api.fetch(video_id)
```

Using the `WebshareProxyConfig` will default to using rotating residential proxies and requires no further 
configuration.

You can also limit the pool of IPs that you will be rotating through to those located in specific countries. By 
choosing locations that are close to the machine that is running your code, you can reduce latency. Also, this 
can be used to work around location-based restrictions. 

```python
ytt_api = YouTubeTranscriptApi(
    proxy_config=WebshareProxyConfig(
        proxy_username="<proxy-username>",
        proxy_password="<proxy-password>",
        filter_ip_locations=["de", "us"],
    )
)

# Webshare will now only rotate through IPs located in Germany or the United States!
ytt_api.fetch(video_id)
```

You can find the 
full list of available locations (and how many IPs are available in each location) 
[here](https://www.webshare.io/features/proxy-locations?referral_code=w0xno53eb50g).

Note that [referral links are used here](https://www.webshare.io/?referral_code=w0xno53eb50g) and any purchases 
made through these links will support this Open Source project (at no additional cost of course!), which is very much 
appreciated! 💖😊🙏💖

However, you are of course free to integrate your own proxy solution using the `GenericProxyConfig` class, if you 
prefer using another provider or want to implement your own solution, as covered by the following section.

### Using other Proxy solutions

Alternatively to using [Webshare](#using-webshare), you can set up any generic HTTP/HTTPS/SOCKS proxy using the 
`GenericProxyConfig` class:

```python
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import GenericProxyConfig

ytt_api = YouTubeTranscriptApi(
    proxy_config=GenericProxyConfig(
        http_url="http://user:pass@my-custom-proxy.org:port",
        https_url="https://user:pass@my-custom-proxy.org:port",
    )
)

# all requests done by ytt_api will now be proxied using the defined proxy URLs
ytt_api.fetch(video_id)
```

Be aware that using a proxy doesn't guarantee that you won't be blocked, as YouTube can always block the IP of your 
proxy! Therefore, you should always choose a solution that rotates through a pool of proxy addresses, if you want to
maximize reliability.

## Overwriting request defaults

When initializing a `YouTubeTranscriptApi` object, it will create a `requests.Session` which will be used for all
HTTP(S) request. This allows for caching cookies when retrieving multiple requests. However, you can optionally pass a
`requests.Session` object into its constructor, if you manually want to share cookies between different instances of
`YouTubeTranscriptApi`, overwrite defaults, set custom headers, specify SSL certificates, etc.

```python
from requests import Session

http_client = Session()

# set custom header
http_client.headers.update({"Accept-Encoding": "gzip, deflate"})

# set path to CA_BUNDLE file
http_client.verify = "/path/to/certfile"

ytt_api = YouTubeTranscriptApi(http_client=http_client)
ytt_api.fetch(video_id)

# share same Session between two instances of YouTubeTranscriptApi
ytt_api_2 = YouTubeTranscriptApi(http_client=http_client)
# now shares cookies with ytt_api
ytt_api_2.fetch(video_id)
```

## Cookie Authentication

> [!WARNING]
> **Cookie Authentication is temporarily disabled and unsupported.**
> Some videos are age restricted, which historically required cookie authentication to access. However, recent changes to the YouTube API broke the implementation of cookie-based auth. As a result, this feature is currently disabled in the codebase (both in the API and CLI wrappers) and passing a cookies file will not work.

## Using Formatters
Formatters are meant to be an additional layer of processing of the transcript you pass it. The goal is to convert a
`FetchedTranscript` object into a consistent string of a given "format". Such as a basic text (`.txt`) or even formats 
that have a defined specification such as JSON (`.json`), WebVTT (`.vtt`), SRT (`.srt`), Comma-separated format 
(`.csv`), etc...

The `formatters` submodule provides a few basic formatters, which can be used as is, or extended to your needs:

- JSONFormatter
- PrettyPrintFormatter
- TextFormatter
- WebVTTFormatter
- SRTFormatter

Here is how to import from the `formatters` module.

```python
# the base class to inherit from when creating your own formatter.
from youtube_transcript_api.formatters import Formatter

# some provided subclasses, each outputs a different string format.
from youtube_transcript_api.formatters import JSONFormatter
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.formatters import WebVTTFormatter
from youtube_transcript_api.formatters import SRTFormatter
```

### Formatter Example
Let's say we wanted to retrieve a transcript and store it to a JSON file. That would look something like this:

```python
# your_custom_script.py

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch(video_id)

formatter = JSONFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(transcript)

# Now we can write it out to a file.
with open('your_filename.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)

# Now should have a new JSON file that you can easily read back into Python.
```

**Passing extra keyword arguments**

Since JSONFormatter leverages `json.dumps()` you can also forward keyword arguments into 
`.format_transcript(transcript)` such as making your file output prettier by forwarding the `indent=2` keyword argument.

```python
json_formatted = JSONFormatter().format_transcript(transcript, indent=2)
```

### Custom Formatter Example
You can implement your own formatter class. Just inherit from the `Formatter` base class and ensure you implement the 
`format_transcript(self, transcript: FetchedTranscript, **kwargs) -> str` and 
`format_transcripts(self, transcripts: List[FetchedTranscript], **kwargs) -> str` methods which should ultimately 
return a string when called on your formatter instance.

```python
class MyCustomFormatter(Formatter):
    def format_transcript(self, transcript: FetchedTranscript, **kwargs) -> str:
        # Do your custom work in here, but return a string.
        return 'your processed output data as a string.'

    def format_transcripts(self, transcripts: List[FetchedTranscript], **kwargs) -> str:
        # Do your custom work in here to format a list of transcripts, but return a string.
        return 'your processed output data as a string.'
```

## CLI

To execute the CLI script (registered via Poetry), prefix the commands with `poetry run`:

```bash  
poetry run youtube_transcript_api <first_video_id> <second_video_id> ...  
```  

The CLI also gives you the option to provide a list of preferred languages:  

```bash  
poetry run youtube_transcript_api <first_video_id> <second_video_id> ... --languages de en  
```

You can also specify if you want to exclude automatically generated or manually created subtitles:

```bash  
poetry run youtube_transcript_api <first_video_id> <second_video_id> ... --languages de en --exclude-generated
poetry run youtube_transcript_api <first_video_id> <second_video_id> ... --languages de en --exclude-manually-created
```

If you would prefer to write it into a file or pipe it into another application, you can also output the results as json:  

```bash  
poetry run youtube_transcript_api <first_video_id> <second_video_id> ... --languages de en --format json > transcripts.json
```  

Translating transcripts using the CLI:

```bash  
poetry run youtube_transcript_api <first_video_id> <second_video_id> ... --languages en --translate de
```  

To list all available transcripts:

```bash  
poetry run youtube_transcript_api --list-transcripts <first_video_id>
```

If a video's ID starts with a hyphen you'll have to mask the hyphen using `\` to prevent the CLI from mistaking it for an argument name. For example:

```bash
poetry run youtube_transcript_api "\-abc123"
```

### Working around IP bans using the CLI

If you are running into `RequestBlocked` or `IpBlocked` errors, you can use rotating residential proxies like [Webshare](https://www.webshare.io/?referral_code=w0xno53eb50g). Run the following command with your credentials:

```bash
poetry run youtube_transcript_api <first_video_id> <second_video_id> --webshare-proxy-username "username" --webshare-proxy-password "password"
```

If you prefer to use another proxy solution, you can set up a generic HTTP/HTTPS proxy:

```bash
poetry run youtube_transcript_api <first_video_id> <second_video_id> --http-proxy http://user:pass@domain:port --https-proxy https://user:pass@domain:port
```

### Cookie Authentication using the CLI

> [!WARNING]
> **Cookie authentication is currently disabled/unsupported.** The `--cookies` option is non-functional because cookie authentication has been commented out in the library code due to YouTube API changes breaking it.

## Warning  

This code uses an undocumented part of the YouTube API, which is called by the YouTube web-client. So there is no 
guarantee that it won't stop working tomorrow, if they change how things work. I will however do my best to make things 
working again as soon as possible if that happens. So if it stops working, let me know!  

## Contributing

To setup the project locally run the following (requires [poetry](https://python-poetry.org/docs/) to be installed):
```shell
poetry install --with test,dev
```

There's [poe](https://github.com/nat-n/poethepoet?tab=readme-ov-file#quick-start) tasks to run tests, coverage, the 
linter and formatter (you'll need to pass all of those for the build to pass):
```shell
poe test
poe coverage
poe format
poe lint
```

If you just want to make sure that your code passes all the necessary checks to get a green build, you can simply run:
```shell
poe precommit
```

## Donations

If this project makes you happy by reducing your development time, you can make me happy by treating me to a cup of 
coffee, or become a [Sponsor of this project](https://github.com/sponsors/jdepoix) :)  

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=BAENLEW8VUJ6G&source=url)

