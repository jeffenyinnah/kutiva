from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from teacher.models import Lesson
from course.models import *

def index(request):
	courses_list = Course.objects.all().order_by('-created_at')

	page = request.GET.get('pagina', 1)

	num_items = 9

	paginator = Paginator(courses_list, num_items)

	try:
		courses = paginator.page(page)
	except PageNotAnInteger:
		courses = paginator.page(1)
		page = 1
	except EmptyPage:
		courses = paginator.page(paginator.num_pages)

	index = courses.number - 1
	max_index = len(paginator.page_range)

	if int(page) <= 3:
		start_index = 0
		end_index = 6
	else: 
		start_index = index - 3 
		end_index = index + 3 if index <= max_index -3 else max_index
	page_range = list(paginator.page_range)[start_index:end_index]

	return render(request, 'kutiva/index.html', {'page_range': page_range,
													  'current_page': page,
													  'paginator': paginator, 
													  'courses': courses, 
													  })
