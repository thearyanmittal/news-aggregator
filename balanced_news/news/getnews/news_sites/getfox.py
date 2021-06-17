from ...models import Headline
import requests
from bs4 import BeautifulSoup

def getfox(per_site):

    fox_html = requests.get('http://www.foxnews.com/politics')
    fox_soup = BeautifulSoup(fox_html.text, 'lxml')

    fox_list = fox_soup.find_all('div', class_='content article-list')
    fox_count = 0
    for lst in fox_list:
        fox = lst.find_all('article', class_='article')
        for article in fox:
            if fox_count < per_site:
                headline = Headline()
                pic = article.find('a').find('img')['src']
                url = article.find('a')['href']
                title = article.find('h4', class_='title').find('a').text
                time_ago = article.find('span', class_='time').text
                leaning = 'right'

                headline.img = pic
                if url[0] == '/':
                    headline.url = "http://www.foxnews.com" + url
                else:
                    headline.url = url
                headline.title = title
                headline.leaning = leaning
                headline.time_ago_str = time_ago
                headline.save()

                fox_count += 1
            
            else:
                break
