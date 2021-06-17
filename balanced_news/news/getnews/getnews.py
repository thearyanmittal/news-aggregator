from .news_sites.getpolitico import getpolitico
from .news_sites.getfox import getfox
from .news_sites.getnatreview import getnatreview
from .news_sites.getslate import getslate
from .news_sites.getcnn import getcnn
from .news_sites.getdailywire import getdailywire


def get_news():
    STORIES = 50 # should be long enough news site
    SITES = 6
    per_site = STORIES // SITES

    getfox(per_site)
    getpolitico(per_site)
    getnatreview(per_site)
    getslate(per_site)
    getcnn(per_site)
    getdailywire(per_site)
