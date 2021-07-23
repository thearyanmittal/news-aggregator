from apscheduler.schedulers.blocking import BlockingScheduler
from balanced_news.news.getnews import getnews

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour='13', minute='6')
def update_headlines():
    getnews()

sched.start()