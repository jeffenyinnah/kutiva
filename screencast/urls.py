from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.screencasts, name="screencasts"),
    path('watch', views.watch, name="watch"),

]
