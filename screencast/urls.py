from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^screencasts', views.screencasts, name="screencasts"),
 	url(r'^watch/(?P<id>\d+)/', views.watch, name="watch"),


]
