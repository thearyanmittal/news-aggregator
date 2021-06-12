from .news_sites.getpolitico import getpolitico
from .news_sites.getfox import getfox
from .news_sites.getnatreview import getnatreview
from .news_sites.getslate import getslate


def get_news():
    STORIES = 50
    SITES = 4
    per_site = STORIES // SITES

    getfox(per_site)
    getpolitico(per_site)
    getnatreview(per_site)
    getslate(per_site)
