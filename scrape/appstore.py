import datetime as dt

import requests
from app_store_scraper import AppStore


def scrape_app_store(country, app_name, size):
    app_id = get_app_id(country, app_name)
    app_ = AppStore(country=country, app_name=app_name, app_id=app_id)
    max_size = int(size) if size else 200

    current_date = dt.date.today()
    app_.review(how_many=max_size,
                after=dt.datetime(current_date.year, current_date.month - 1, 1),
                sleep=None)

    reviews = app_.reviews
    results = []
    for review in reviews:
        rev = review['review']
        results.append(rev)

    return results


def get_app_id(country, app_name):
    url = "https://itunes.apple.com/search"
    params = {
        'term': app_name,
        'country': country,
        'media': 'software',
        'entity': 'software',
        'limit': 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data['resultCount'] > 0:
        app_id = data['results'][0]['trackId']
        return app_id
    else:
        return None
