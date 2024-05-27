from django.contrib import admin
from portfolio.models import WebsiteInfo, CarouselImages, Category, Projects, ProjectImage

class WebsiteInfoAdmin(admin.ModelAdmin):
    list_display = ("index_title", "about_title", "date")

    def has_add_permission(self, request):
        if WebsiteInfo.objects.exists():
            return False
        return True
    
class CarouselImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "alt", "date")

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "display_online", "date")
    search_fields = ('project_name',)
    list_filter = ('categories',)
    inlines = [ProjectImageInline]
   
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")

admin.site.register(WebsiteInfo, WebsiteInfoAdmin)
admin.site.register(CarouselImages, CarouselImagesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Projects, ProjectsAdmin)
