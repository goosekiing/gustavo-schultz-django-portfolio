from django.db import models
from django.utils import timezone
from solo.models import SingletonModel

class WebsiteInfo(SingletonModel):
    index_title = models.CharField(max_length=256, null=True, blank=True)
    index_text = models.TextField(default="", null=False, blank=True)
    about_title = models.CharField(max_length=256, default="About Me", null=False, blank=True)
    about_text = models.TextField(default="", null=False, blank=False)
    about_picture = models.ImageField(upload_to='images/about/%Y/%m/%d', blank=True)
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
    date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class ProjectImage(models.Model):
    project = models.ForeignKey(Projects, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/projects/%Y/%m/%d', blank=True)

    def __str__(self):
        return f"Imagem do projeto {self.project.name}"
    
    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Image"
