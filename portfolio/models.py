from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

class Projects(models.Model):

    project_name = models.CharField(max_length=128, null=False, blank=False)
    categories = models.ManyToManyField(Category)
    description = models.TextField(default="", null=False, blank=False)
    github_link = models.URLField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.project_name
