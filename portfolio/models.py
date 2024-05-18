from django.db import models
from django.utils import timezone
from solo.models import SingletonModel

class About(SingletonModel):
    text = models.TextField(default="", null=False)
    picture = models.ImageField(upload_to='images/about/%Y/%m/%d', blank=True)
    date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return "About Me Model"
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Projects(models.Model):

    name = models.CharField(max_length=128, null=False, blank=False)
    categories = models.ManyToManyField(Category)
    description = models.TextField(default="", null=False, blank=True)
    github_link = models.URLField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to='images/projects/%Y/%m/%d', blank=True)
    date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class Contact(SingletonModel):
    whatsapp_link = models.URLField(max_length=256, blank=False, null=False)
    github_link = models.URLField(max_length=256, blank=False, null=False)
    linkedin_link = models.URLField(max_length=256, blank=False, null=False)
    email = models.CharField(max_length=128, null=False, blank=False)
    date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return "About Me Model"
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"
