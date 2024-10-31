from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def scrape_twitter(topic):
    eml = '22206052001@student.uin-suka.ac.id'
    usr = '@dennyafr170713'
    pwd = 'man.utd1878'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://x.com/i/flow/login")

    wait = WebDriverWait(browser, 20)
    username = wait.until(EC.presence_of_element_located(
        (By.XPATH,
         "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")))
    username.send_keys(eml)

    next_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]")))
    next_button.click()

    try:
        second_username = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")))
        second_username.send_keys(usr)

        next_button2 = wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button")))
        next_button2.click()
    except Exception as e:
        print("Kullanıcı adı istenmedi, doğrudan şifre ekranına geçiliyor...")

    password = wait.until(EC.presence_of_element_located(
        (By.XPATH,
         "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")))
    password.send_keys(pwd)

    login = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")))
    login.click()

    try:
        search = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input")))
        search.send_keys(topic)
        search.send_keys(Keys.RETURN)

        results = []
        time.sleep(5)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        tweets = soup.select("[data-testid='tweetText']")

        for tweet in tweets[:5]:
            tweet_id = tweet.find_parent("article")["data-tweet-id"]
            comments = get_comments(browser, tweet_id)
            results.append(comments)

        browser.quit()
        return results
    except Exception as e:
        print("Terdapat error: " + e)
        browser.quit()
        return []


def get_comments(browser, tweet_id):
    browser.get(f"https://x.com/{tweet_id}/with_replies")
    time.sleep(5)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    replies = soup.select("[data-testid='reply']")

    comments = [reply.get_text() for reply in replies]
    return comments
