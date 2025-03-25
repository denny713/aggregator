import requests
from bs4 import BeautifulSoup


def scrape_stack_overflow(type, keyword, size):
    query = keyword.replace(" ", "-")
    base_url = 'https://stackoverflow.com'
    url = '{}/questions/tagged/{}'.format(base_url, query)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup_content = soup.find_all('h3', class_='s-post-summary--content-title')

    results = []
    record = 0
    for scontent in soup_content:
        record += 1
        link = scontent.find('a', class_='s-link').get('href')
        content_response = requests.get(base_url + link)
        content_soup = BeautifulSoup(content_response.content, 'html.parser')
        content = ""
        if type == "topic":
            content = scontent.text
        elif type == "question":
            question_soup = content_soup.find('div', class_='s-prose js-post-body')
            content = question_soup.text
        elif type == "answer":
            try:
                answers_soup = content_soup.find_all('div', class_='s-prose js-post-body')
                for answer in answers_soup:
                    content = answer.text
            except Exception as e:
                continue
        else:
            content = "-"

        layout_soup = content_soup.find('div', class_='postcell post-layout--right')
        user_tag = layout_soup.select_one('span.d-none[itemprop="name"]')
        user = user_tag.text.strip() if user_tag else None
        timestamp_tag = layout_soup.find("div", class_="user-action-time").find("span")
        timestamp = timestamp_tag["title"].split(" ")[0]

        results.append({
            'user': user,
            'timestamp': timestamp,
            'rating': '-',
            'content': content,
            'preview': content
        })

        if size != "" and int(size) == record:
            break

    return results
