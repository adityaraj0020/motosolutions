
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([x['text'] for x in transcript])
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    video_ids = [
        "uVt6z1zF4aQ",  # Replace with real R15 repair video IDs
        "yFQlvbSejRU"
    ]
    for vid in video_ids:
        print(f"Transcript for {vid}:\n")
        print(get_transcript(vid))
        print("\n" + "="*80 + "\n")
