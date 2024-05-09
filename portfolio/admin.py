from django.contrib import admin
from portfolio.models import Category, Projects

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("id", "project_name", "description", "date")
    search_fields = ('project_name',)
    list_filter = ('category',)
   
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Projects, ProjectsAdmin)
