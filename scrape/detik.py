import re
import urllib

import requests
from bs4 import BeautifulSoup


def scrape_detik(type, keyword, size):
    results = []
    max_page = int(size) if size else 50

    for page in range(1, max_page):
        query = urllib.parse.quote_plus(keyword)
        url = 'https://www.detik.com/search/searchnews?query={}&sortby=time&page={}'.format(query, page)
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        texts = soup.find_all('div', class_='media__text')
        for text in texts:
            content = ""
            if type == "title":
                content = text.find('a', class_='media__link').text.strip()
            elif type == "resume":
                content = text.find('div', class_='media__desc').text.strip()

            link = text.find('a', href=True)['href']
            detail_response = requests.get(link)
            detail_soup = BeautifulSoup(detail_response.content, "html.parser")
            detail_header = detail_soup.find('div', class_='detail__header')
            if (detail_header):
                author_text = detail_header.find('div', class_='detail__author').text.strip()
                author = author_text.split(" - ")[0]
                date_str = detail_header.find('div', class_='detail__date').text.strip()
                match = re.search(r'(\d{2}) (\w+) (\d{4})', date_str)
                if match:
                    day, month_str, year = match.groups()
                    months = {
                        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "Mei": "05", "Jun": "06",
                        "Jul": "07", "Agu": "08", "Sep": "09", "Okt": "10", "Nov": "11", "Des": "12"
                    }
                    month = months.get(month_str[:3], "01")
                    formatted_date = f"{year}-{month}-{day}"
                else:
                    formatted_date = "Format tanggal tidak valid"

                results.append({
                    'user': author,
                    'timestamp': formatted_date,
                    'rating': '',
                    'content': content,
                    'preview': content
                })

            else:
                print("Header element tidak ditemukan")

            if len(results) >= max_page:
                break

        if len(results) >= max_page:
            break

    return results
