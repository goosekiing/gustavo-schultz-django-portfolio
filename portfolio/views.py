from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Count
from portfolio.models import WebsiteInfo, CarouselImages, Projects, Category

def index(request):
    website_info = WebsiteInfo.objects.first()
    carousel_loops = 10
    carousel_images = CarouselImages.objects.all()
    carousel_images_list = list(carousel_images) * carousel_loops
    carousel_images_count = carousel_images.count() * carousel_loops
    context = {
        'website_info': website_info,
        'carousel_images': carousel_images_list,
        'carousel_images_count': carousel_images_count,
        'carousel_loops': carousel_loops
    }
    return render(request, "portfolio/index.html", context)

def about(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/about.html", {'website_info': website_info})

def portfolio(request):
    projects = Projects.objects.order_by("-date").filter(display_online=True)
    categories = Category.objects.annotate(project_count=Count('projects')).filter(project_count__gt=0)
    selected_tag = None
    context = {
        'projects': projects,
        'categories': categories,
        'selected_tag': selected_tag}
    return render(request, "portfolio/portfolio.html", context)

def category(request, category_slug ):
    category_obj = get_object_or_404(Category, slug=category_slug)
    projects = Projects.objects.order_by("-date").filter(display_online=True, categories=category_obj)
    categories = Category.objects.annotate(project_count=Count('projects')).filter(project_count__gt=0)
    selected_tag = category_slug
    context = {
        'projects': projects,
        'categories': categories,
        'selected_tag': selected_tag}
    return render(request, "portfolio/portfolio.html", context)

def project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    if project.display_online:
        tag = request.GET.get('tag')
        display_carousel_buttons = True if project.images.count() > 1 else False
        context = {
            'project': project,
            'tag': tag,
            'display_carousel_buttons': display_carousel_buttons
            }
        return render(request, "portfolio/project.html", context)
    raise Http404("Error: project id not found")

def contact(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/contact.html", {'website_info': website_info})
