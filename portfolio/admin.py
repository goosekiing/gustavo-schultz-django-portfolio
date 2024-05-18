from django.contrib import admin
from portfolio.models import About, Category, Projects, Contact

class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "date")

    def has_add_permission(self, request):
        if About.objects.exists():
            return False
        return True

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "date")
    search_fields = ('project_name',)
    list_filter = ('categories',)
   
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "whatsapp_link", "github_link", "linkedin_link", "email", "date")

    def has_add_permission(self, request):
        if Contact.objects.exists():
            return False
        return True

admin.site.register(About, AboutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Contact, ContactAdmin)
