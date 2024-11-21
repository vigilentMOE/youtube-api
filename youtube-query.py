import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    """extract video ID from YouTube URL"""
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
    return None

def get_recommendations(youtube, video_id, max_results=10):
    """get video recommendations using search"""
    request = youtube.search().list(
        part="snippet",
        type="video",
        maxResults=max_results,
        # Using search terms from the original video
        q=get_video_title(youtube, video_id)
    )
    return request.execute()

def get_video_title(youtube, video_id):
    """get the title of the video to use as search term"""
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    if response['items']:
        return response['items'][0]['snippet']['title']
    return ""

def main():
    # load API key from .env
    load_dotenv()
    api_key = os.getenv('YOUTUBE_API_KEY')
    
    if not api_key:
        print("error: API key not found in .env file")
        return
    
    # initialize YouTube API
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # get video URL from user
    url = input("enter YouTube video URL: ")
    video_id = extract_video_id(url)
    
    if not video_id:
        print("invalid YouTube URL")
        return
    
    # get recommendations
    try:
        recommendations = get_recommendations(youtube, video_id)
        
        print("\n=== Recommended Videos ===\n")
        for item in recommendations['items']:
            title = item['snippet']['title']
            channel = item['snippet']['channelTitle']
            description = item['snippet']['description'][:200] + '...'
            video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            
            print(f"📺 {title}")
            print(f"👤 {channel}")
            print(f"📝 {description}")
            print(f"🔗 {video_url}")
            print("-" * 50 + "\n")
            
    except Exception as e:
        print(f"an error occurred: {str(e)}")

if __name__ == "__main__":
    main()