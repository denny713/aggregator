import urllib

import requests
from bs4 import BeautifulSoup


def scrape_springer(type, keyword, size):
    max_size = int(size) if size else 300
    query = urllib.parse.quote_plus(keyword)
    global_url = 'https://link.springer.com'
    url = '{}/search/page/1?facet-content-type=Article&query={}'.format(global_url, query)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    results = []
    titles = soup.find_all("a", class_="title")
    for title in titles:
        link = global_url + title["href"]
        article = requests.get(link)
        article_soup = BeautifulSoup(article.content, "html.parser")

        date_element = article_soup.find('time')
        timestamp = date_element['datetime']

        author_list = [a.get_text(strip=True) for a in
                       article_soup.select('li.c-article-author-list__item a[data-test="author-name"]')]
        authors = ', '.join(author_list)

        if type == "title":
            content = title.text.strip()
        else:
            content = article_soup.find("div", class_="c-article-section__content").text.strip()

        results.append({
            'user': authors,
            'timestamp': timestamp,
            'rating': '',
            'content': content,
            'preview': content
        })

        if len(results) == max_size:
            break
    else:
        results = []

    return results
