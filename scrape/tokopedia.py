import time
import urllib

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def get_window_cache_items(browser):
    return browser.execute_script("return window.__cache;")


def scrape_tokopedia(type, keyword, size):
    max_size = int(size) if size else 300
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=chrome_options)

    results = []
    if type == "toko":
        url_toko = 'https://www.tokopedia.com/{}/review'.format(keyword)
        browser.get(url_toko)
        time.sleep(3)

        while len(results) < max_size:
            cache_item = get_window_cache_items(browser)

            for key, value in cache_item.items():
                user = ""
                comment = ""
                rating = ""

                if key.startswith("shopReviewList"):
                    if value.get("reviewText"):
                        comment = value.get("reviewText")
                    if value.get("reviewerName"):
                        user = value.get("reviewerName")
                    if value.get("rating"):
                        rating = value.get("rating")

                    if comment.strip() and user.strip() and rating is not None:
                        results.append({
                            'user': user,
                            'timestamp': '',
                            'rating': rating,
                            'content': comment,
                            'preview': comment
                        })

                if len(results) == max_size:
                    break

            try:
                next_button = WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "button.css-16uzo3v-unf-pagination-item[aria-label='Laman berikutnya']"))
                )

                next_button.click()
                WebDriverWait(browser, 10).until(
                    lambda driver: driver.execute_script("return window.__cache;") != cache_item
                )
            except Exception:
                print("Tidak bisa klik tombol Next atau halaman sudah habis.")
                break

        browser.quit()
    elif type == "produk":
        query = urllib.parse.quote_plus(keyword)
        url_produk = 'https://www.tokopedia.com/search?st=&q={}&page=1'.format(query)
        browser.get(url_produk)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zeus-root')))
        time.sleep(2)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        produk_soup = BeautifulSoup(browser.page_source, "html.parser")
        product_elements = produk_soup.find_all('div', class_='css-5wh65g')

        for element in product_elements:
            product_name_elm = element.find('span', class_='_0T8-iGxMpV6NEsYEhwkqEg==')
            product_name = product_name_elm.text.strip() if product_name_elm else "-"

            rating_elm = element.find('span', class_='_9jWGz3C-GX7Myq-32zWG9w==')
            rating = rating_elm.text.strip() if rating_elm else "0"

            user_elm = element.find('span', class_='T0rpy-LEwYNQifsgB-3SQw== pC8DMVkBZGW7-egObcWMFQ== flip')
            user = user_elm.text.strip() if user_elm else "-"

            results.append({
                'user': user,
                'timestamp': '',
                'rating': rating,
                'content': product_name,
                'preview': product_name
            })

            if len(results) == max_size:
                break

        browser.quit()
    else:
        results = []

    return results
