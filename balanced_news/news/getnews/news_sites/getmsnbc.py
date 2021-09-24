from ...models import Headline
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dateparser import parse

def getmsnbc(per_site):
    
    msnbc_html = requests.get('https://www.msnbc.com/').text
    msnbc_soup = BeautifulSoup(msnbc_html, 'lxml')

    msnbc_list = list(msnbc_soup.find_all('div', 'styles_featuredArticle__33zGR')) + list(
        msnbc_soup.find_all('div', class_='styles_gridItem__11MlF layout-grid-item grid-col-6-m'))
    
    msnbc_count = 0
    for art in msnbc_list:
        if msnbc_count < per_site:
            headline = Headline()

            headline.leaning = 'left'
            headline.title = art.find('h3').find('a').text
            headline.url = art.find('a')['href']
            headline.img = art.find('img')['src']
            
            time_soup = BeautifulSoup(requests.get(headline.url).text, 'lxml')
            pubdt = parse(time_soup.find('time').text.split(',', 2)[0])

            if pubdt.date() < datetime.now().date():
                headline.time_ago_str = 'before today'
            else:
                headline.time_ago_str = 'recently'

            headline.save()
            msnbc_count += 1

if __name__ == '__main__':
    getmsnbc(15)