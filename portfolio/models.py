from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from solo.models import SingletonModel
from datetime import datetime
import os

def about_picture_path(instance, filename):
    return os.path.join(settings.ABOUT_PICTURE_DIR, filename)

def carousel_image_path(instance, filename):
    return os.path.join(settings.CAROUSEL_IMAGES_DIR, filename)

def project_image_path(instance, filename):
    date_path = datetime.now().strftime(settings.PROJECT_IMAGE_DIR)
    return os.path.join(date_path, filename)

class WebsiteInfo(SingletonModel):
    index_title = models.CharField(max_length=256, null=True, blank=True)
    index_text = models.TextField(default="", null=False, blank=True)
    about_title = models.CharField(max_length=256, default="About Me", null=False, blank=True)
    about_text = models.TextField(default="", null=False, blank=False)
    about_picture = models.ImageField(upload_to=about_picture_path, blank=True)
    about_picture_alt = models.CharField(max_length=256, default="", blank=True)
    portfolio_title = models.CharField(max_length=256, null=True, blank=True)
    contact_title = models.CharField(max_length=256, null=True, blank=True)
    whatsapp_link = models.URLField(max_length=256, blank=True, null=True)
    github_link = models.URLField(max_length=256, blank=True, null=True)
    linkedin_link = models.URLField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return "Website Index, About Me and Contact Info Model"
    
    class Meta:
        verbose_name = "Website Info"
        verbose_name_plural = "Website Info"

class CarouselImages(models.Model):
    image = models.ImageField(upload_to=carousel_image_path, null=False, blank=False)
    alt = models.CharField(max_length=256, default="", blank=True)
    date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.alt if self.alt != "" else f'Carousel Image {self.id}'
    
    class Meta:
        verbose_name = "Carousel Image"
        verbose_name_plural = "Carousel Images"

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False, blank=False)
    slug = models.SlugField(default="", max_length=64, null=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Projects(models.Model):
    name = models.CharField(max_length=128, default="", unique=True, null=False, blank=False)
    categories = models.ManyToManyField(Category, blank=True)
    description = models.TextField(default="", null=False, blank=True)
    github_link = models.URLField(max_length=128, blank=True, null=True)
    display_online = models.BooleanField(default=True)
    develop_date = models.DateField(null=True, blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class ProjectImage(models.Model):
    project = models.ForeignKey(Projects, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=project_image_path, blank=True)
    alt = models.CharField(max_length=256, default="", blank=True)

    def __str__(self):
        return f"Imagem do projeto {self.project.name}"
    
    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Image"
