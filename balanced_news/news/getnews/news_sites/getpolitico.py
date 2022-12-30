from ...models import Headline
import requests
from bs4 import BeautifulSoup
import datetime
from dateparser import parse

def getpolitico(per_site):
    politico_html = requests.get('http://www.politico.com/politics')
    politico_soup = BeautifulSoup(politico_html.text, 'lxml')

    politico = politico_soup.find_all('article', class_='story-frag format-sm')
    politico_count = 0
    for article in politico:
        if len(article.find('a').text.split(" ")) > 4  and politico_count < per_site and 'politico' not in article.find('a').text.lower():
            headline = Headline()
            if article.find('img') != None:
                pic = article.find('img')['src']
            else:
                pic = ""
            url = article.find('a')['href']
            title = article.find('a').text
            leaning = 'left'

            now = datetime.datetime.now()
            pub_datetime_str = article.find('time')['datetime']
            pub_datetime = parse(pub_datetime_str)
            time_ago = (now - pub_datetime).seconds // 60

            headline.img = pic
            headline.url = url
            headline.title = title
            headline.leaning = leaning
            headline.mins_ago = time_ago + 60 #for some reason, always short 1hr
            headline.save()
            
            politico_count += 1
