import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from selenium import webdriver
def go_request():
    options = webdriver.ChromeOptions()
    # open it, go to a website, and get results
    wd = webdriver.Chrome('chromedriver', options=options)
    wd.get("https://fanyi.baidu.com/#zh/en/%E4%BD%A0%E5%A5%BD")
    print(wd.page_source)  # results


