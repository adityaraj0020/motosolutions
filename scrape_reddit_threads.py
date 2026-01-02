
import requests

def fetch_reddit_posts(subreddit="Yamaha", query="R15 issue", limit=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.reddit.com/r/{subreddit}/search.json?q={query}&restrict_sr=1&sort=relevance&t=all&limit={limit}"
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        for post in data['data']['children']:
            print("Title:", post['data']['title'])
            print("Text:", post['data'].get('selftext', ''))
            print("----")
    else:
        print("Failed to fetch:", res.status_code)

if __name__ == "__main__":
    fetch_reddit_posts()
