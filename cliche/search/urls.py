from django.urls import path
from django.conf.urls import include, url
from . import views
urlpatterns = [
    path('',  views.search, name="home"),

    #search is a name link in url :: http://localhost:8000/search/?q=tube
    url(r'^search/$', views.list),


]
