from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class Subject(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.subject


class Category(models.Model):
    category = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.category


class Lesson(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    subject = models.ManyToManyField(Subject)
    category = models.ManyToManyField(Category)
    cover = models.ImageField(upload_to='images')
    video = EmbedVideoField(blank=True)
    date = models.DateField(default=timezone.now())
    """docstring for Lesson"""


class Course(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    subject = models.ManyToManyField(Subject)
    category = models.ManyToManyField(Category)
    lesson = models.ManyToManyField(Lesson)
    cover = models.ImageField(upload_to='images')
    date = models.DateField(default=timezone.now())
    """docstring for Lesson"""

# # Create your models here.
