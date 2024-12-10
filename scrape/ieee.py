import json
import urllib
from datetime import datetime

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
    print(articles)

    results = []
    if response.status_code == 200:
        for article in articles:
            authors = article.get("authors", {}).get("authors", [])
            author_names = [author.get("full_name", "") for author in authors]
            author_list = ', '.join(author_names)

            date_obj = datetime.strptime(article['insert_date'], "%Y%m%d")
            formatted_date = date_obj.strftime("%Y-%m-%d")
            timestamp = formatted_date

            if type == "title":
                content = article['title']
            else:
                content = article['abstract']

            results.append({
                'user': author_list,
                'timestamp': timestamp,
                'rating': '',
                'content': content
            })

    else:
        print(f"Error: Unable to fetch the content. Status code: {response.status_code}")
        results = []

    return results
