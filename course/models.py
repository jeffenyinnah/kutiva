import django
from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class Subject(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    subject = models.ManyToManyField(Subject)
    category = models.ManyToManyField(Category)
    cover = models.ImageField(upload_to='images')
    video = EmbedVideoField(blank=True)
    date = models.DateField(default=django.utils.timezone.now)


    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    subject = models.ManyToManyField(Subject)
    category = models.ManyToManyField(Category)
    lesson = models.ManyToManyField(Lesson)
    cover = models.ImageField(upload_to='images')
    date = models.DateField(default=django.utils.timezone.now)
    """docstring for Lesson"""

    def __str__(self):
        return self.title
