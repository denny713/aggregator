import json
import time
import urllib
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_product_code(url):
    try:
        last_segment = url.rstrip('/').split('/')[-1]
        return last_segment.split('-')[0]
    except IndexError:
        return ""


def scrape_bukalapak(type, keyword, size):
    max_size = int(size) if size else 300
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=chrome_options)

    browser.get("https://www.bukalapak.com")
    time.sleep(5)

    local_storage_data = browser.execute_script("return window.localStorage;")
    bl_token = json.loads(local_storage_data['bl_token'])
    access_token = bl_token['access_token']

    browser.quit()

    results = []

    if type == "produk":
        query = urllib.parse.quote_plus(keyword)
        url_toko = 'https://www.bukalapak.com/products/s?brand_badge=false&campaign_name=&page=1&search%5Bkeywords%5D={}'.format(
            query)
        response_toko = requests.get(url_toko)
        soup_toko = BeautifulSoup(response_toko.content, 'html.parser')
        links = soup_toko.find_all('a', class_='slide')
        for link in links:
            product_code = get_product_code(link['href'])
            if product_code == "":
                continue

            product_url = f'https://api.bukalapak.com/product-reviews?limit={max_size}&offset=0&product_id={product_code}&access_token={access_token}'
            product_response = requests.get(product_url)
            response = product_response.json()
            datas = response.get("data", [])

            if not datas:
                continue

            for data in datas:
                user = data.get("sender", {}).get("name", "Unknown User")
                rating = data.get("review", {}).get("rate", "No rating")
                title = data.get("review", {}).get("title", "")
                content = data.get("review", {}).get("content", "")
                review = f"{title} {content}".strip()

                created_at_str = data.get("created_at", "")
                try:
                    created_at = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                    timestamp = created_at.strftime("%Y-%m-%d")
                except ValueError:
                    timestamp = ""

                results.append({
                    'user': user,
                    'timestamp': timestamp,
                    'rating': rating,
                    'content': review,
                    'preview': review
                })

                if len(results) == max_size:
                    break

            if len(results) == max_size:
                break

    elif type == "toko":
        query = urllib.parse.quote_plus(keyword)
        url_toko = 'https://www.bukalapak.com/{}'.format(query)
        response_toko = requests.get(url_toko)
        soup_toko = BeautifulSoup(response_toko.content, 'html.parser')
        products = soup_toko.find_all('div', class_='revamp-c-card c-card')
        for product in products:
            product_link = product.find('a',
                                        class_='c-product-card__name js-tracker-product-link u-mrgn-top--2 u-mrgn-bottom--1 c-product-card__ellipsis c-product-card__ellipsis-2')
            product_code = get_product_code(product_link['href'])
            product_url = f'https://api.bukalapak.com/product-reviews?limit={max_size}&offset=0&product_id={product_code}&access_token={access_token}'
            product_response = requests.get(product_url)
            response = product_response.json()
            datas = response.get("data", [])

            if not datas:
                continue

            for data in datas:
                user = data.get("sender", {}).get("name", "Unknown User")
                rating = data.get("review", {}).get("rate", "No rating")
                title = data.get("review", {}).get("title", "")
                content = data.get("review", {}).get("content", "")
                review = f"{title} {content}".strip()

                created_at_str = data.get("created_at", "")
                try:
                    created_at = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                    timestamp = created_at.strftime("%Y-%m-%d")
                except ValueError:
                    timestamp = ""

                results.append({
                    'user': user,
                    'timestamp': timestamp,
                    'rating': rating,
                    'content': review,
                    'preview': review
                })

                if len(results) == max_size:
                    break

            if len(results) == max_size:
                break

    else:
        results = []

    return results
