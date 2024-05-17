from django.contrib import admin
from portfolio.models import About, Category, Projects

class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "date")

    def has_add_permission(self, request):
        return False

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "date")
    search_fields = ('project_name',)
    list_filter = ('categories',)
   
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)

admin.site.register(About, AboutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Projects, ProjectsAdmin)
