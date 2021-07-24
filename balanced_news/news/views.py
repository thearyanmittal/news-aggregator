from django.shortcuts import render
from .models import Headline
from .getnews.getnews import get_news
import random
from rq import Queue
from worker import conn


def shownews(request):
    
    q = Queue(connection=conn)
    q.enqueue(get_news)

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)
