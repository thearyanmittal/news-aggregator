from ...models import Headline
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateparser import parse

def getnypost(per_site):
    html = requests.get('https://nypost.com/news/').text
    soup = BeautifulSoup(html, 'lxml')

    articles = soup.find_all('div', class_='story story--archive story--i-flex')

    count = 0
    for art in articles:
        if count < per_site:
            headline = Headline()
            headline.leaning = 'right'
            headline.title = art.find('h3').text.strip()
            headline.img = art.find('img')['src']
            headline.url = art.find('a')['href']

            timestr = art.find('span', class_='meta meta--byline').text.strip()
            pubdt = parse(timestr)
            time_ago = datetime.now() - pubdt
            headline.mins_ago = int(time_ago.total_seconds() // 60)

            headline.save()
            count += 1
        else:
            break
