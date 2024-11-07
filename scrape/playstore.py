from google_play_scraper import reviews, Sort, search


def scrape_play_store(country, app_name, size):
    lang = 'id' if country == 'id' else 'en'
    size = int(size) if size else 200
    print(lang)

    app_id = get_app_id(app_name)
    if not app_id:
        print("App ID not found.")
        return []

    rvws, _ = reviews(
        app_id,
        lang=lang,
        country=country,
        sort=Sort.NEWEST,
        count=int(size)
    )

    results = []
    records = 0
    for rvw in rvws:
        records += 1
        rev = rvw['content']
        results.append(rev)

        if size != "" and int(size) == records:
            break

    return results


def get_app_id(app_name):
    results = search(app_name, lang='en', country='us')
    if results:
        app_id = results[0]['appId']
        print(app_id)
        return app_id
    else:
        print("Not found")
        return None
