# YouTube Video Recommender

A Python script that fetches video recommendations based on a YouTube video URL using the YouTube Data API v3.

## Features

- Extract video IDs from various YouTube URL formats
- Fetch video recommendations based on the original video's title
- Display recommended videos with title, channel, description, and URL
- Environment variable support for API key management

## Prerequisites

- Python 3.6+
- Google Cloud project with YouTube Data API v3 enabled
- YouTube API key

## Installation

```bash
pip install google-api-python-client python-dotenv
```

## Configuration

1. Create a `.env` file in the project root
2. Add your YouTube API key:
```
YOUTUBE_API_KEY=your_api_key_here
```

## Usage

```python
python youtube-query.py
```

When prompted, enter a YouTube video URL. The script will display recommended videos with their details.
