from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('screencasts', views.screencasts, name="screencasts"),
    path('watch/<id>', views.watch, name="watch"),

]
