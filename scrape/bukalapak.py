import urllib

import requests
from bs4 import BeautifulSoup


def scrape_bukalapak(type, keyword, size):
    results = []
    max_size = int(size) if size else 300
    if type == "produk":
        query = urllib.parse.quote_plus(keyword)
        url_produk = 'https://www.bukalapak.com/products/s?brand_badge=false&campaign_name=&page=1&search%5Bkeywords%5D={}'.format(
            query)
        response_produk = requests.get(url_produk)
        soup_produk = BeautifulSoup(response_produk.content, 'html.parser')
        links = soup_produk.find_all('a', class_='slide')
        for link in links:
            detail_produk = requests.get(link['href'])
            detail_produk_soup = BeautifulSoup(detail_produk.content, 'html.parser')
            comments = detail_produk_soup.find_all('p', {"data-testid": "content"})
            for comment in comments:
                comment_text = comment.text
                if comment_text != "" and comment_text is not None:
                    results.append(comment_text)
    elif type == "toko":
        url_toko = 'https://www.bukalapak.com/u/{}/feedback?feedback_as=as_seller&filter_by=all'.format(keyword)
        response_toko = requests.get(url_toko)
        soup_toko = BeautifulSoup(response_toko.content, 'html.parser')
        soup_toko_content = soup_toko.find_all('p', class_='bl-text bl-text--body-default')

        for content in soup_toko_content:
            results.append(content.text)
    else:
        results = []

    return results
