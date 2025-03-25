from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def scrape_facebook(url_req, size):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=chrome_options)

    max_size = int(size) if size else 300
    url = 'https://facebook.com'
    username = "suka.enelpe@gmail.com"
    password = "Sukanlp123."
    browser.get(url)

    wait = WebDriverWait(browser, 30)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_field.send_keys(username)
    pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
    pass_field.send_keys(password)
    pass_field.send_keys(Keys.RETURN)

    time.sleep(5)
    browser.get(url_req)
    time.sleep(10)

    results = []
    try:
        time.sleep(5)
        comments = browser.find_elements(By.XPATH,
                                         "//div[contains(@class, 'xwib8y2') and contains(@class, 'xn6708d')]")

        for comment in comments:
            try:
                user = comment.find_element(By.XPATH, ".//span[contains(@class, 'x3nfvp2')]").text
            except:
                user = "Unknown User"

            try:
                content = comment.find_element(By.XPATH, ".//div[contains(@class, 'xdj266r')]").text
            except:
                content = "No content"

            results.append({
                'user': user,
                'timestamp': '',
                'rating': '',
                'content': content,
                'preview': content
            })

            if len(results) >= max_size:
                break

    except Exception as e:
        print(f"Terjadi error: {e}")

    browser.quit()
    return results
