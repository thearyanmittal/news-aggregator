from django.shortcuts import render
from news.models import Headline
import datetime
import requests
from bs4 import BeautifulSoup
import lxml

def get_news():
    STORIES = 50
    sites = 2
    per_site = STORIES // sites

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

    
    politico_html = requests.get('http://www.politico.com/politics')
    politico_soup = BeautifulSoup(politico_html.text, 'lxml')

    politico = politico_soup.find_all('article', class_='story-frag format-sm')
    politico_count = 0
    for article in politico:
        if len(article.find('a').text.split(" ")) > 4  and politico_count < per_site:
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
            pub_datetime = datetime.datetime.strptime(pub_datetime_str, '%Y-%m-%d %H:%M:%S')
            time_ago = (now - pub_datetime).seconds // 60

            headline.img = pic
            headline.url = url
            headline.title = title
            headline.leaning = leaning
            headline.mins_ago = time_ago
            headline.save()
            
            politico_count += 1



def index(request):
    Headline.objects.all().delete()
    get_news()
    headlines = Headline.objects.order_by('?')
    context = {
        'headline_list': headlines,
        'num_headlines': len(headlines) #for debugging purposes
    }
    return render(request, 'news/news.html', context=context)
