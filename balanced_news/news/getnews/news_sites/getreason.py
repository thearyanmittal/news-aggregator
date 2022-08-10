from ...models import Headline
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dateparser import parse

def getreason(per_site):
    
    reason_html = requests.get('https://reason.com/latest/').text
    reason_soup = BeautifulSoup(reason_html, 'lxml')

    reason_list = reason_soup.find_all('article')

    reason_count = 0
    for art in reason_list:
        if reason_count < per_site:
            headline = Headline()
            headline.leaning = 'right'
            headline.title = art.find('h4').text.strip()
            headline.img = art.find('img')['data-lazy-src']
            headline.url = art.find('a')['href']

            time_str = art.find('time').text
            pubdt = parse(time_str)
            time_ago = (datetime.now() - pubdt).total_seconds()
            headline.mins_ago = int(time_ago // 60)

            headline.save()
            reason_count += 1
