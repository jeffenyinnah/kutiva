from django.contrib import admin

from course.models import Category


class CategoryItem(admin.ModelAdmin):
    list_display = ['name']
    # search_fields = ['name']


admin.site.register(Category, CategoryItem)


