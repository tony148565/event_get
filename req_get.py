import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

d = {'key1': 'value1', 'key2': 'value2'}
man_url = ''


def get_html(url, url2):
    headers = {'referer': url2, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    r = requests.post(url, data=json.dumps(d), headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_sel_html(url):
    driver_path = r"C:\Chrome_driver\chromedriver.exe"
    driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
    cc = driver.page_source
    driver.close()
    return cc
