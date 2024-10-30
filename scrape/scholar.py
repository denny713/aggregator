import json
import urllib

import requests


def scrape_google_scholar(type, keyword):
    api_key = '1609213ef166691bcb0751578113d82586a0b8d9d16c446de7768091fde9808d'
    query = urllib.parse.quote_plus(keyword)
    url = ('https://serpapi.com/search?engine=google_scholar&q={}&api_key={}'.format(query, api_key))
    response = requests.get(url)
    response_data = json.loads(response.text)['organic_results']

    results = []
    for result in response_data:
        if type == "title":
            results.append(result['title'])
        elif type == "abstract":
            results.append(result['snippet'])
        else:
            results = []

    return results
