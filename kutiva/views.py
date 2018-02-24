from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
# from teacher.models import Lesson


def index(request):
    # lessons = Lesson.objects.all()
    # {'lessons': lessons}
    return render(request, 'kutiva/index.html')
