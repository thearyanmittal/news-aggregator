from apscheduler.schedulers.blocking import BlockingScheduler
from balanced_news.news.getnews import getnews
from balanced_news.news.models import Headline

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour='12', minute='50')
def update_headlines():
    Headline.objects.all().delete()
    getnews()

sched.start()