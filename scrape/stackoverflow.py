import requests
from bs4 import BeautifulSoup


def scrape_stack_overflow(type, keyword):
    query = keyword.replace(" ", "-")
    base_url = 'https://stackoverflow.com'
    url = '{}/questions/tagged/{}'.format(base_url, query)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup_content = soup.find_all('h3', class_='s-post-summary--content-title')

    results = []
    for scontent in soup_content:
        link = scontent.find('a', class_='s-link').get('href')
        content_response = requests.get(base_url + link)
        content_soup = BeautifulSoup(content_response.content, 'html.parser')
        if type == "topic":
            results.append(scontent.text)
        elif type == "question":
            question_soup = content_soup.find('div', class_='s-prose js-post-body')
            results.append(question_soup.text)
        elif type == "answer":
            try:
                answers_soup = content_soup.find_all('div', class_='s-prose js-post-body')
                for answer in answers_soup:
                    results.append(answer.text)
            except Exception as e:
                continue
        else:
            results = []

    return results
