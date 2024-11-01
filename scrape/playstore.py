from google_play_scraper import reviews, Sort, search


def scrape_play_store(app_name):
    count = 200
    rvws, _ = reviews(
        get_app_id(app_name),
        lang='id',
        country='id',
        sort=Sort.NEWEST,
        count=count
    )

    results = []
    for rvw in rvws:
        rev = rvw['content']
        results.append(rev)

    return results


def get_app_id(app_name):
    results = search(app_name, lang='en', country='us')

    if results:
        app_id = results[0]['appId']
        return app_id
    else:
        return None
