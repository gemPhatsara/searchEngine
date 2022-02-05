from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
urlpatterns = [
    path('index/', views.index),
    path('', include('search.urls'))

]
