import urllib

import requests
from bs4 import BeautifulSoup


def scrape_springer(type, keyword):
    query = urllib.parse.quote_plus(keyword)
    global_url = 'https://link.springer.com'
    url = '{}/search/page/1?facet-content-type=Article&query={}'.format(global_url, query)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    results = []
    if type == "title":
        titles = soup.find_all("a", class_="title")

        for title in titles:
            results.append(title.text.strip())
    elif type == "abstract":
        titles = soup.find_all("a", class_="title")

        for title in titles:
            link = global_url + title["href"]
            article = requests.get(link)
            article_soup = BeautifulSoup(article.content, "html.parser")
            abstract = article_soup.find("div", class_="c-article-section__content")
            results.append(abstract.text.strip())
    else:
        results = []

    return results
