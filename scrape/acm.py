import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def scrape_acm(type, keyword, size):
    base_url = 'https://dl.acm.org'
    url = '{}/action/doSearch?AllField={}'.format(base_url, keyword)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=chrome_options)

    browser.get(url)
    time.sleep(5)
    max_size = int(size) if size else 300
    soup = BeautifulSoup(browser.page_source, "html.parser")
    browser.quit()

    results = []
    articles = soup.find_all('li', class_='search__item issue-item-container')
    for article in articles:
        authors = ', '.join([author.text for author in article.find_all('span', class_='hlFld-ContribAuthor')])
        date_str = article.find('div', class_='bookPubDate').text.strip()
        date_obj = datetime.strptime(date_str, '%B %Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        if type == "title":
            content = article.find('h3', class_='issue-item__title').text.strip()
        else:
            browser_detail = webdriver.Chrome(options=chrome_options)
            abstract = soup.find("h3", class_="issue-item__title")
            link = abstract.find('a', href=True)['href']
            detail_uri = base_url + link
            browser_detail.get(detail_uri)
            time.sleep(5)
            detail_soup = BeautifulSoup(browser_detail.page_source, "html.parser")
            content = detail_soup.find("div", attrs={"role": "paragraph"}).text
            browser_detail.quit()

        results.append({
            'user': authors,
            'timestamp': formatted_date,
            'rating': '',
            'content': content,
            'preview': content
        })

        if len(results) == max_size:
            break

    return results
