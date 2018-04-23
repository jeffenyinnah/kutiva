from django.shortcuts import render
from .models import  *
# Create your views here.


def course(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    return render(request,'course/index.html',{"courses": courses, 'categories':categories})