# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Category(models.Model):
	name  = models.CharField(max_length=50, unique=True)
	image = models.FileField(upload_to='images/category', max_length=200, blank=True, null=True)
	slug  = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class Subcategory(models.Model):
	name 	 = models.CharField(max_length=50, unique=True)
	category = models.ForeignKey(Category, models.CASCADE)
	slug 	 = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class Lesson(models.Model):
	title 	 = models.CharField(max_length=50)
	url 	 = models.URLField(max_length=500)
	duration = models.TimeField(blank=True, null=True)

	def __str__(self):
		return self.title

class Level(models.Model):
	name 	 = models.CharField(max_length=50, unique=True)
	slug 	 = models.CharField(unique=True, max_length=250)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name 	 = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class Course(models.Model):
	title 		= models.CharField(max_length=250)
	Subcategory	= models.ForeignKey(Subcategory, models.CASCADE)
	description = models.CharField(max_length=250)
	cover		= models.FileField(upload_to='images/courses/cover', max_length=200, blank=True, null=True)
	lessons 	= models.ForeignKey(Lesson, models.CASCADE)
	level 		= models.ForeignKey(Level, models.CASCADE)
	duration 	= models.TimeField(blank=True, null=True)
	views 		= models.IntegerField(default=0)
	tags 		= models.ManyToManyField(Tag, related_name='related_tag')
	slug 	    = models.CharField(unique=True, max_length=250)
	is_active   = models.BooleanField(default=True)
	author 		= models.ManyToManyField(User, related_name='related_user')
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)
	updated_by  = models.ForeignKey(User, models.CASCADE, related_name='course_updator', blank=True, null=True)
	created_by  = models.ForeignKey(User, models.CASCADE, related_name='course_creator', blank=True, null=True) 

	def __str__(self):
		return self.title

