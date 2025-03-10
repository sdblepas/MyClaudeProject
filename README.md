# YouTube Video Downloader

A simple Python script to download YouTube videos using pytube library.

## Features

- Download videos in different resolutions
- Progress bar for download status
- Command-line interface for easy usage
- Simple error handling

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/sdblepas/MyClaudeProject.git
   cd MyClaudeProject
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Advanced Options

```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -o /path/to/save -r 720p
```

### Command Line Arguments

- `url`: YouTube video URL (required)
- `-o, --output`: Directory to save the video (optional, defaults to current directory)
- `-r, --resolution`: Video resolution (optional, defaults to highest available)
  - Options: "highest", "lowest", or specific resolution like "720p"

## Examples

```bash
# Download with highest resolution to current directory
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Download with specific resolution to a specific folder
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -o ~/Videos -r 480p

# Download with lowest resolution
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -r lowest
```

## Legal Notice

This tool is for educational purposes only. Please respect copyright laws and the YouTube Terms of Service. Only download videos that you have permission to download.

## License

MIT