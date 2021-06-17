from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from ...models import Headline
import os

def getdailywire(per_site):
    PATH = os.environ['CHROMEDRIVER_PATH']
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

    with driver as dv:
        dv.get('https://www.dailywire.com/read')
        source = dv.page_source

    soup = BeautifulSoup(source, 'lxml')
    articles = soup.find('div', class_='css-1wjvcxq e1fyft6w0').find_all('article')

    count = 0
    for art in articles:
        if count < per_site:
            headline = Headline()
            headline.leaning = 'right'
            headline.title = art.find('h3').text
            headline.img = art.find('img')['src']
            headline.url = art.find('a')['href']
            headline.time_ago_str = 'recently'
            headline.save()

            count += 1
        else:
            break
        