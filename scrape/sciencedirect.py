import json
import urllib

import requests
from bs4 import BeautifulSoup


def scrape_science_direct(type, keyword):
    api_key = '7f59af901d2d86f78a1fd60c1bf9426a'
    query = urllib.parse.quote_plus(keyword)
    url = 'https://api.elsevier.com/content/search/sciencedirect?query={}&apiKey={}'.format(query, api_key)
    response = requests.get(url)
    json_data = json.loads(response.text)
    datas = json_data['search-results']['entry']
    results = []

    for data in datas:
        if type == "title":
            results.append(data['dc:title'])
        else:
            pii = data['pii']
            link = 'https://api.elsevier.com/content/article/pii/{}?apiKey={}'.format(pii, api_key)


    return results
