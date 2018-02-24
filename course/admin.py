# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from .models import (
	Category, 
	Subcategory, 
	Lesson, 
	Level, 
	Tag, 
	Course
	)


class CourseResource(resources.ModelResource):

    class Meta:
        model= Course

class CourseAdmin(ImportExportActionModelAdmin):
    resource_class = CourseResource
    list_display=(
                       "id",
                       "title",
                       "created_by",
                       "created_at",
                    )
    search_fields=(
                        "title",
                        "author",
                    )
    pass


# Adds models yto admin site
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Lesson)
admin.site.register(Level)
admin.site.register(Tag)
admin.site.register(Course, CourseAdmin)

