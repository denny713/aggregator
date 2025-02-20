from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def scrape_twitter(url_req, size):
    eml = '22206052001@student.uin-suka.ac.id'
    usr = '@dennyafr170713'
    pwd = 'man.utd1878'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=chrome_options)

    try:
        browser.get("https://x.com/i/flow/login")
        wait = WebDriverWait(browser, 15)

        username_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='text']")))
        username_input.send_keys(eml)
        browser.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(2)

        try:
            username_input = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']"))
            )
            username_input.send_keys(usr)
            browser.find_element(By.XPATH, "//span[text()='Next']").click()
            time.sleep(2)
        except Exception:
            print("Username tidak diminta, langsung ke password")

        password_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='password']")))
        password_input.send_keys(pwd)
        browser.find_element(By.XPATH, "//span[text()='Log in']").click()
        time.sleep(5)

        browser.get(url_req)
        time.sleep(5)

        results = []
        max_size = int(size) if size else 300

        while len(results) < max_size:
            tweets = browser.find_elements(By.XPATH, "//article[@data-testid='tweet']")

            for tweet in tweets:
                try:
                    username = tweet.find_element(By.XPATH, ".//div[@data-testid='User-Name']//span").text
                    timestamp = tweet.find_element(By.XPATH, ".//time").get_attribute("datetime")
                    comment = tweet.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text

                    results.append({
                        'user': username,
                        'timestamp': timestamp[:10],
                        'rating': '',
                        'content': comment,
                        'preview': comment
                    })

                    if len(results) >= max_size:
                        break

                except Exception:
                    continue

            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        return results[:max_size]

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

    finally:
        browser.quit()
