import urllib

import requests
from bs4 import BeautifulSoup


def scrape_detik(type, keyword):
    results = []

    for page in range(1, 3):
        query = urllib.parse.quote_plus(keyword)
        url = 'https://www.detik.com/search/searchnews?query={}&sortby=time&page={}'.format(query, page)
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        if type == "title":
            titles = soup.find_all("h3", class_="media__title")

            for title in titles:
                results.append(title.text.strip())
        elif type == "topic":
            topics = soup.find_all("div", class_="media__desc")

            for topic in topics:
                results.append(topic.text.strip())
        else:
            results = []

    return {"data": results}
