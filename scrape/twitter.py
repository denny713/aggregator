from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def scrape_twitter(url_req):
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
        print("Nama pengguna tidak diminta, langsung ke layar kata sandi...")

    password = wait.until(EC.presence_of_element_located(
        (By.XPATH,
         "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")))
    password.send_keys(pwd)

    login = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")))
    login.click()

    time.sleep(5)
    browser.get(url_req)
    time.sleep(10)
    results = []
    try:
        time.sleep(5)
        comments = browser.find_elements(By.XPATH,
                                         "//div[@class='css-146c3p1 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim']")
        for comment in comments:
            results.append(comment.text)

    except Exception as e:
        print(f"Terjadi error: {e}")

    return results
