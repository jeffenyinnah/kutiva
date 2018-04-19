# from django.db import models
# from django.forms import ModelForm
# from django.utils import timezone
#
#
# class Subject(models.Model):
#     subject = models.CharField(max_length=100)
#     date = models.DateField(default=timezone.now())
#
#     def __str__(self):
#         return self.subject
#
#
# class Category(models.Model):
#     category = models.CharField(max_length=100)
#     date = models.DateField(default=timezone.now())
#
#     def __str__(self):
#         return self.category
#
#
# class Screencast(models.Model):
#     title = models.CharField(max_length=300)
#     description = models.TextField()
#     subjects = models.ManyToManyField(Subject)
#     categories = models.ManyToManyField(Category)
#     cover = models.ImageField(upload_to='images')
#     video = models.FileField(upload_to='videos')
#     date = models.DateField(default=timezone.now())
#     """docstring for Lesson"""
#
#
#
#
# # # Create your models here.