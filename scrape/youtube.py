from datetime import datetime

from googleapiclient.discovery import build


def scrape_youtube(keyword, size):
    api_key = 'AIzaSyB1Vil81Cp4pFYU6IynwYqynBo9t1CCn2c'
    youtube = build('youtube', 'v3', developerKey=api_key)

    search_response = youtube.search().list(
        q=keyword,
        part='id,snippet',
        maxResults=10
    ).execute()

    max_size = int(size) if size else 300
    results = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video_id = search_result['id']['videoId']

            try:
                comments = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    textFormat='plainText',
                    maxResults=max_size
                ).execute()

                for comment in comments['items']:
                    comment_snippet = comment['snippet']['topLevelComment']['snippet']
                    comment_text = comment_snippet['textDisplay']
                    comment_user = comment_snippet['authorDisplayName']
                    timestamp = comment_snippet['publishedAt']
                    dt_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
                    formatted_date = dt_object.strftime("%Y-%m-%d")

                    results.append({
                        'user': comment_user,
                        'timestamp': formatted_date,
                        'rating': '',
                        'content': comment_text,
                        'preview': comment_text
                    })

                    if len(results) == max_size:
                        break
            except:
                print("Fitur komentar dinonaktifkan oleh pemilik video")
                continue

            if len(results) == max_size:
                break

    return results
