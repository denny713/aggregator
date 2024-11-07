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

    url = 'https://facebook.com'
    username = "suka.enelpe@gmail.com"
    password = "Sukanlp123."
    browser.get(url)

    wait = WebDriverWait(browser, 3600)
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
        record = 0
        comments = browser.find_elements(By.XPATH, "//div[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs']")
        for comment in comments:
            record += 1
            results.append(comment.text)

            if size != "" and int(size) == record:
                break

    except Exception as e:
        print(f"Terjadi error: {e}")

    return results
