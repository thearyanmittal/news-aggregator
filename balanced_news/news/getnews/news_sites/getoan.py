<<<<<<< HEAD
from ...models import Headline
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dateparser import parse

def getoan(per_site):

    oan_html = requests.get('https://www.oann.com/category/newsroom/').text
    oan_soup = BeautifulSoup(oan_html, 'lxml')

    oan_list = oan_soup.find_all('article')

    oan_count = 0
    for art in oan_list:
        if oan_count < per_site:
            headline = Headline()
            headline.leaning = 'right'
            headline.title = art.text.strip()
            headline.img = art.find('img')['src']
            headline.url = art.find('a')['href']

            time_soup = BeautifulSoup(requests.get(headline.url).text, 'lxml')
            try:
                pubdt = parse(time_soup.find('h5').text.split('UPDATED')[1]) # wrap in try block to work

                if pubdt.date() < datetime.now().date():
                    headline.time_ago_str = 'before today'
                else:
                    headline.time_ago_str = 'recently'
            except:
                headline.time_ago_str = 'recently'

            headline.save()
            oan_count += 1
        
        else:
=======
from ...models import Headline
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dateparser import parse

def getoan(per_site):

    oan_html = requests.get('https://www.oann.com/category/newsroom/').text
    oan_soup = BeautifulSoup(oan_html, 'lxml')

    oan_list = oan_soup.find_all('article')

    oan_count = 0
    for art in oan_list:
        if oan_count < per_site:
            headline = Headline()
            headline.leaning = 'right'
            headline.title = art.text.strip()
            headline.img = art.find('img')['src']
            headline.url = art.find('a')['href']

            time_soup = BeautifulSoup(requests.get(headline.url).text, 'lxml')
            try:
                pubdt = parse(time_soup.find('h5').text.split('UPDATED')[1])
            except:
                pubdt = datetime.now()

            if pubdt.date() < datetime.now().date():
                headline.time_ago_str = 'before today'
            else:
                headline.time_ago_str = 'recently'

            headline.save()
            oan_count += 1
        
        else:
>>>>>>> a60eb6fa5e379bddb23620c5fc8ea5c746a2f6a3
            break