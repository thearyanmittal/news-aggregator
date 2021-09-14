from ...models import Headline
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from dateparser import parse

def getnatreview(per_site):
    url = 'https://www.nationalreview.com/latest/'
    url2 = 'https://www.nationalreview.com/latest/page/2/'

    html = requests.get(url).text
    html2 = requests.get(url2).text

    soup = BeautifulSoup(html, 'lxml')
    soup2 = BeautifulSoup(html2, 'lxml')

    articles = soup.find_all('article') + soup2.find_all('article')
    i = 0
    for art in articles:
        if i < per_site:
            headline = Headline()
            headline.leaning = 'right'
            headline.title = art.find('h4', class_='post-list-article__title').text
            headline.img = art.find('figure').find('img')['src']
            headline.url = art.find('a')['href']

            if ':' in (timestr := art.find('time').text):
                time_ago = parse(timestr).time()

                if time_ago < (datetime.now() - timedelta(days=1)).time():
                    delta = datetime.now() - timedelta(hours=time_ago.hour, minutes=time_ago.minute, seconds=time_ago.second)
                    headline.mins_ago = delta.hour*60 + delta.minute
                else:
                    headline.mins_ago = 1441

            else:
                headline.mins_ago = 1441

            headline.save()
            i += 1

        else:
            break
