from .news_sites.getpolitico import getpolitico
from .news_sites.getfox import getfox
from .news_sites.getnatreview import getnatreview
from .news_sites.getslate import getslate
from .news_sites.getcnndailywire import getcnndailywire
from .news_sites.getnypost import getnypost
from .news_sites.getnpr import getnpr
from ..models import Headline


def get_news():
    STORIES = 75
    SITES = 8
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    getfox(per_site)
    getpolitico(per_site)
    getnatreview(per_site)
    getslate(per_site)
    getnypost(per_site)
    getnpr(per_site)
    # getcnndailywire(per_site)