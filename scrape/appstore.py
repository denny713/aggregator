import datetime as dt

import requests
from app_store_scraper import AppStore


def scrape_app_store(app_name):
    app_id = get_app_id(app_name)
    app_ = AppStore(country='id', app_name=app_name, app_id=app_id)

    current_date = dt.date.today()
    app_.review(how_many=20,
                after=dt.datetime(current_date.year, current_date.month - 1, 1),
                sleep=None)

    reviews = app_.reviews
    results = []
    for review in reviews:
        rev = review['review']
        results.append(rev)

    return results


def get_app_id(app_name):
    url = "https://itunes.apple.com/search"
    params = {
        'term': app_name,
        'country': 'id',
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