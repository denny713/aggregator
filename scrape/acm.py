from datetime import datetime

import requests
from bs4 import BeautifulSoup


def scrape_acm(type, keyword, size):
    base_url = 'https://dl.acm.org'
    url = '{}/action/doSearch?AllField={}'.format(base_url, keyword)
    response = requests.get(url)
    max_size = int(size) if size else 300

    results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all('li', class_='search__item issue-item-container')

        for article in articles:
            authors = ', '.join([author.text for author in article.find_all('span', class_='hlFld-ContribAuthor')])
            date_str = article.find('div', class_='bookPubDate').text.strip()
            date_obj = datetime.strptime(date_str, '%B %Y')
            formatted_date = date_obj.strftime('%Y-%m-%d')
            if type == "title":
                content = article.find('h5', class_='issue-item__title').text.strip()
            else:
                abstract = soup.find("h5", class_="issue-item__title")
                link = abstract.find('a', href=True)['href']
                detail_uri = base_url + link
                detail_response = requests.get(detail_uri)
                detail_soup = BeautifulSoup(detail_response.content, "html.parser")
                content = detail_soup.find("div", attrs={"role": "paragraph"}).text

            results.append({
                'user': authors,
                'timestamp': formatted_date,
                'rating': '',
                'content': content,
                'preview': content
            })

            if len(results) == max_size:
                break
    else:
        print(f"Error: Unable to fetch the content. Status code: {response.status_code}")
        results = []

    return results
