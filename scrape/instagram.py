from instagrapi import Client


def scrape_instagram(keyword):
    client = Client()
    username = 'suka.enelpe@gmail.com'
    password = 'Sukanlp123.'
    client.login(username, password)

    results = []

    medias = client.hashtag_medias_recent(keyword, 5)
    for media in medias:
        comments = client.media_comments(media.pk)
        for comment in comments:
            results.append(comment.text)

    return results
