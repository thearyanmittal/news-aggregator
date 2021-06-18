from ...models import Headline
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def getnypost(per_site):
    html = requests.get('https://nypost.com/news/').text
    soup = BeautifulSoup(html, 'lxml')

    articles = soup.find('ul', class_='article-loop').find_all('li', class_='half')

    count = 0
    for art in articles:
        if count < per_site:
            headline = Headline()
            headline.leaning = 'right'
            headline.title = art.find('h3').text.strip()
            headline.img = art.find('source')['data-srcset'].split(' 2x')[0]
            headline.url = art.find('a')['href']

            timestr = art.find('div', class_='entry-meta').text.strip()
            pubdt = datetime.strptime(timestr, "%B %d, %Y | %I:%M%p")
            time_ago = datetime.now() - pubdt
            headline.mins_ago = int(time_ago.total_seconds() // 60)

            headline.save()
            count += 1
        else:
            break
