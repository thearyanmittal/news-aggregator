"""balanced_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
import os
from . import settings
import numpy as np

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sources(request):
    IMG_BASE_DIR = os.path.abspath(os.path.join(settings.STATICFILES_DIRS[0], 'media/newslist'))

    img_names = [os.path.join('media/newslist', name) for name in os.listdir(IMG_BASE_DIR)]
    img_sites = [f"https://www.{name.split('-')[0]}.com/" if not name.startswith('npr')
    else f"https://www.{name.split('-')[0]}.org/" for name in os.listdir(IMG_BASE_DIR)]

    img_srcs = np.array_split(np.array(list(zip(img_sites, img_names))), 2)


    context = {'img_srcs': img_srcs}
    return render(request, 'sources.html', context=context)

urlpatterns = [
    path('news/', include('news.urls')),
    path('register/', include('register.urls')),
    path('about/', about),
    path('sources/', sources),
    path('admin/', admin.site.urls),
    path('', about),
    path('home/', home),
    path('', include("django.contrib.auth.urls")),
]
