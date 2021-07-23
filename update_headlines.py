from apscheduler.schedulers.blocking import BlockingScheduler
from balanced_news.news.getnews import getnews

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=120)
def update_headlines():
    getnews()

sched.start()