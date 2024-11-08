import json
import urllib

import requests


def scrape_google_scholar(type, keyword, size):
    max_size = int(size) if size else 300
    api_key = '1609213ef166691bcb0751578113d82586a0b8d9d16c446de7768091fde9808d'
    query = urllib.parse.quote_plus(keyword)
    url = ('https://serpapi.com/search?engine=google_scholar&q={}&num={}&api_key={}'.format(query, max_size, api_key))
    response = requests.get(url)
    response_data = json.loads(response.text)['organic_results']

    results = []
    for result in response_data:
        if type == "title":
            results.append(result['title'])
        elif type == "abstract":
            detail_link = result['inline_links']['cited_by']['serpapi_scholar_link']
            detail_uri = ('{}&api_key={}'.format(detail_link, api_key))
            detail_response = requests.get(detail_uri)
            detail_response_data = json.loads(detail_response.text)['organic_results']
            abstract = " ".join(item["snippet"].replace("…", "") for item in detail_response_data)
            results.append(abstract)
        else:
            results = []

    return results
