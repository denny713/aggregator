import json
import urllib

import requests
import xmltodict


def scrape_science_direct(type, keyword, size):
    headers = {
        "Accept": "application/xml",
        "X-ELS-APIKey": "69691fd2a98b018877fe90d4d922b315",
        "X-ELS-Insttoken": "7b239acf049df2b930f8fe8fc331d0d2",
        'Cookie': '__cf_bm=68HlFrvAa8VWZickduad8eTYRKyqZLqKI.0UNLEEr4Q-1696542666-0-AYrM1Pzt1jwXzBkZTD7BeiJKSLRYOKAyWZtt6KTg+rCCKgr6CpLrCkje+JyY81qXnxnSWo4tS/Lc/mbWYlfeINE='
    }

    max_size = int(size) if size else 300
    query = urllib.parse.quote_plus(keyword)
    url = 'https://api.elsevier.com/content/search/sciencedirect?query={}'.format(query)
    response = requests.request("GET", url, headers=headers, data={})
    data_dict = xmltodict.parse(response.text)
    json_data = json.dumps(data_dict, indent=4, sort_keys=True)
    json_object = json.loads(json_data)
    datas = json_object['search-results']['entry']
    results = []

    for data in datas:
        authors_data = data.get('authors', {}).get('author', [])
        if isinstance(authors_data, list):
            authors = ', '.join(
                [author.get('#text', '') if isinstance(author, dict) else author for author in authors_data])
        elif isinstance(authors_data, dict):
            authors = authors_data.get('#text', '')
        else:
            authors = authors_data if isinstance(authors_data, str) else ''

        timestamp = data.get('prism:coverDate', 'N/A')

        if type == "title":
            content = data.get('dc:title', 'N/A')
        else:
            pii = data['pii']
            if pii:
                link = 'https://api.elsevier.com/content/article/pii/{}'.format(pii)
                resp = requests.request("GET", link, headers=headers)
                if resp.status_code == 200:
                    resp_dict = xmltodict.parse(resp.text)
                    resp_data = json.dumps(resp_dict, indent=4, sort_keys=True)
                    resp_object = json.loads(resp_data)
                    content = resp_object.get('full-text-retrieval-response', {}).get('coredata', {}).get(
                        'dc:description', 'N/A')
                else:
                    content = 'Content tidak tersedia'
            else:
                content = 'PII tidak ditemukan'

        results.append({
            'user': authors,
            'timestamp': timestamp,
            'rating': '',
            'content': content
        })

        if len(results) == max_size:
            break

    return results
