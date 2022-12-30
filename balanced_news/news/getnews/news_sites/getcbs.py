from ...models import Headline
from bs4 import BeautifulSoup
import requests

def getcbs(per_site):
    
    cbs_html = requests.get('https://www.cbsnews.com/').text
    cbs_soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = list(cbs_soup.find_all('article', class_='item--type-article')) + list(
        cbs_soup.find_all('article', class_='item--type-updating_story'))

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('h4').text.strip()
            headline.img = art.find('img')['src']
            headline.url = art.find('a')['href']

            time_ago = art.find('li', class_='item__date').text
            if '1H' in time_ago:
                headline.time_ago_str = time_ago.replace('H', ' hour')
            elif 'ago' not in time_ago:
                headline.time_ago_str = 'before today'
            else:
                headline.time_ago_str = time_ago.replace('M', ' mins').replace('H', ' hours')

            headline.save()
            cbs_count += 1
