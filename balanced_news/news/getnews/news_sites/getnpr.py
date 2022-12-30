from ...models import Headline
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateparser import parse

def getnpr(per_site):
    html = requests.get('https://www.npr.org/sections/news/').text
    soup = BeautifulSoup(html, 'lxml')

    articles = soup.find_all('article', class_='has-image')

    count = 0
    for art in articles:
        if count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('h2').text
            headline.img = art.find('img')['src']
            headline.url = art.find('a')['href']

            time_soup = BeautifulSoup(requests.get(headline.url).text, 'lxml')
            pubdt = parse(time_soup.find('span', class_='time').text[:-3])
            
            if pubdt.date() < datetime.now().date():
                headline.time_ago_str = 'before today'
            else:
                headline.time_ago_str = 'recently'

            headline.save()
            count += 1
        else:
            break