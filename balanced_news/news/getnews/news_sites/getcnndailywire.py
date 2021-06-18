from selenium import webdriver
from bs4 import BeautifulSoup
from ...models import Headline
import os

def getcnndailywire(per_site):

    PATH = os.environ['CHROMEDRIVER_PATH']
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

    with driver as dv:
        dv.get('https://www.cnn.com/politics')
        cnn_source = dv.page_source
        dv.get('https://www.dailywire.com/read')
        dw_source = dv.page_source

    cnn_soup = BeautifulSoup(cnn_source, 'lxml')
    dw_soup = BeautifulSoup(dw_source, 'lxml')
    cnn_articles = cnn_soup.find_all('article', class_='cd--idx-0')
    dw_articles = dw_soup.find('div', class_='css-1wjvcxq e1fyft6w0').find_all('article')

    cnn_count = 0
    for art in cnn_articles:
        if cnn_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span', class_='cd__headline-text').text
            headline.img = art.find('img')['data-src-large']
            headline.url = "https://www.cnn.com/" + art.find('a')['href']
            headline.time_ago_str = 'recently'
            headline.save()

            cnn_count += 1
        else:
            break

    dw_count = 0
    for art in dw_articles:
        if dw_count < per_site:
            headline = Headline()
            headline.leaning = 'right'
            headline.title = art.find('h3').text
            headline.img = art.find('img')['src']
            headline.url = art.find('a')['href']
            headline.time_ago_str = 'recently'
            headline.save()

            dw_count += 1
        else:
            break
        