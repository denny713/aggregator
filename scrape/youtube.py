from googleapiclient.discovery import build


def scrape_youtube(keyword, size):
    api_key = 'AIzaSyB1Vil81Cp4pFYU6IynwYqynBo9t1CCn2c'
    youtube = build('youtube', 'v3', developerKey=api_key)

    search_response = youtube.search().list(
        q=keyword,
        part='id,snippet',
        maxResults=10
    ).execute()

    results = []
    record = 0
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video_id = search_result['id']['videoId']

            try:
                comments = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    textFormat='plainText',
                    maxResults=100
                ).execute()

                for comment in comments['items']:
                    record += 1
                    comment_snippet = comment['snippet']['topLevelComment']['snippet']
                    comment_text = comment_snippet['textDisplay']
                    results.append(comment_text)

                    if size != "" and int(size) == record:
                        break
            except:
                print("Fitur komentar dinonaktifkan oleh pemilik video")
                continue

            if size != "" and int(size) == record:
                break

    return results
