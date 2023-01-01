# News Aggregator
This is a news aggregator web application built with the Django framework. It scrapes news articles (using BeautifulSoup and Selenium) from websites on both sides of the political spectrum and presents them to the user in one webpage.

The site was live at balancednews.us, until Heroku shut down its free tier.

## Usage
Clone the repository and install all required packages in a virtual environment using `pipenv install`. Then, `cd` into the `balanced_news` directory and run `python3 manage.py runserver`. The web app should then be live at [127.0.0.1:8000](127.0.0.1:8000).

## Motivation
As today's political climate becomes more and more polarized, it becomes more difficult for this generation of citizens to find unbiased sources of news. Moreover, popular tech-based news services (such as Google, Facebook, YouTube, and others) tend to personalize content recommendations, causing even the most open-minded to only hear one side of every story and get stuck in intellectual echo-chambers.

Balanced News was founded with the aim of eliminating such echo-chambers by presenting users with news from both sides of the political spectrum in a single space. Articles drawn from multiple sources, representing both liberal and conservative opinions, and covering a variety of hot topics are presented as equals on the News page in form of clickable cards.

## Demo
![News Page Demo](https://raw.githubusercontent.com/thearyanmittal/news-aggregator/main/demo.png)
