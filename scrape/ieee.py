import json
import urllib

import requests


def scrape_ieee(type, keyword, size):
    api_key = '6hu2a2ms42qzx8thtvz52mzk'
    query = urllib.parse.quote_plus(keyword)
    max_record = int(size) if size else 300
    uri_api = ('http://ieeexploreapi.ieee.org/api/v1/search/articles?max_records={}&querytext={}&apikey={}'
               .format(max_record, query, api_key))
    response = requests.get(uri_api)
    response_data = json.loads(response.text)
    articles = response_data['articles']

    results = []
    if response.status_code == 200:
        for article in articles:
            if type == "title":
                results.append(article['title'])
            else:
                results.append(article['abstract'])
    else:
        print(f"Error: Unable to fetch the content. Status code: {response.status_code}")
        results = []

    return results
