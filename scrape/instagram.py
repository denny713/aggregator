from instagrapi import Client


def scrape_instagram(keyword, size):
    client = Client()
    username = 'suka.enelpe@gmail.com'
    password = 'Sukanlp123.'
    client.login(username, password)

    results = []

    record = 0
    medias = client.hashtag_medias_recent(keyword, 5)
    for media in medias:
        comments = client.media_comments(media.pk)
        for comment in comments:
            record += 1
            results.append(comment.text)

            if size != "" and int(size) == record:
                break

        if size != "" and int(size) == record:
            break

    return results
