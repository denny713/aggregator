import time
import urllib

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def scrape_tokopedia(type, keyword, size):
    max_size = int(size) if size else 300
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=chrome_options)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    results = []
    if type == "toko":
        url_toko = 'https://www.tokopedia.com/{}/review'.format(keyword)
        browser.get(url_toko)
        window_cache = browser.execute_script("return window.__cache;")
        review_texts = [
            value["reviewText"] for key, value in window_cache.items()
            if key.startswith("shopReviewList") and value.get("reviewText")
        ]
        results = review_texts
        browser.quit()
    elif type == "produk":
        query = urllib.parse.quote_plus(keyword)
        url_produk = 'https://www.tokopedia.com/search?st=&q={}&page=1'.format(query)
        browser.get(url_produk)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zeus-root')))
        time.sleep(2)
        produk_soup = BeautifulSoup(browser.page_source, "html.parser")
        product_elements = produk_soup.find_all('div', class_='css-5wh65g')
        browser.quit()
        for element in product_elements:
            link = element.find('a', {"data-theme": "default"})
            if link is not None:
                produk_detail = requests.request("GET", link['href'], headers=header)
                produk_detail_soup = BeautifulSoup(produk_detail.content, "html.parser")
                comments = produk_detail_soup.find_all('h1', class_='css-1xfedof')
                for comment in comments:
                    comment_text = comment.text
                    if comment_text != "" and comment_text is not None:
                        results.append(comment_text)
    else:
        results = []

    return results
