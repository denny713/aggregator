import json
import urllib

import requests
import xmltodict


def scrape_book_online(type, keyword):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    api_key = 'Uxb0zPb86N4STVy2ECWYA'
    query = urllib.parse.quote_plus(keyword)
    url = 'https://www.goodreads.com/search.xml?key={}&q={}'.format(api_key, query)
    response = requests.request("GET", url, headers=header, data={})
    data_dict = xmltodict.parse(response.text)
    json_data = json.dumps(data_dict, indent=4, sort_keys=True)
    json_object = json.loads(json_data)
    datas = json_object['GoodreadsResponse']['search']['results']

    results = []
    if type == "title":
        results = [book['best_book']['title'] for book in datas['work']]
    else:
        book_ids = [book['best_book']['id']['#text'] for book in datas['work']]
        print(book_ids)
        for book_id in book_ids:
            book_url = 'https://www.goodreads.com/book/show.xml?key={}&id={}'.format(api_key, book_id)
            book_response = requests.request("GET", book_url, headers=header, data={})
            book_dict = xmltodict.parse(book_response.text)
            json_book = json.dumps(book_dict, indent=4, sort_keys=True)
            book_json = json.loads(json_book)
            book_desc = book_json['GoodreadsResponse']['book']['description']
            results.append(book_desc)

    return results
