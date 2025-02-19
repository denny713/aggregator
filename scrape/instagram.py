from instagrapi import Client


def scrape_instagram(keyword, size):
    client = Client()
    username = 'suka.enelpe@gmail.com'
    password = 'Sukanlp123.'
    client.login(username, password)

    max_size = int(size) if size else 300
    results = []

    medias = client.hashtag_medias_recent(keyword, 5)
    for media in medias:
        comments = client.media_comments(media.pk)
        for comment in comments:
            user = comment.user.username
            content = comment.text
            timestamp = comment.created_at_utc
            formatted_date = timestamp.strftime("%Y-%m-%d")
            rating = comment.like_count

            results.append({
                'user': user,
                'timestamp': formatted_date,
                'rating': rating,
                'content': content,
                'preview': content
            })

            if len(results) == max_size:
                break

        if len(results) == max_size:
            break

    return results
