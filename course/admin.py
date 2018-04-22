from django.contrib import admin

from course.models import *


class CategoryItem(admin.ModelAdmin):
    list_display = ['name']
    # search_fields = ['name']


admin.site.register(Category, CategoryItem)


class SubjectItem(admin.ModelAdmin):
    list_display = ['name']
    # search_fields = ['name']


admin.site.register(Subject, SubjectItem)


class LessonItem(admin.ModelAdmin):
    list_display = ['title']
    # search_fields = ['name']


admin.site.register(Lesson, LessonItem)


class CourseItem(admin.ModelAdmin):
    list_display = ['title']
    # search_fields = ['name']


admin.site.register(Course, CourseItem)


