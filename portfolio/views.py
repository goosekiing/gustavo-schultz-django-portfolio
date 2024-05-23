from django.shortcuts import render, get_object_or_404
from django.http import Http404
from portfolio.models import WebsiteInfo, Projects, Category

def index(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/index.html", {'website_info': website_info})

def about(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/about.html", {'website_info': website_info})

def portfolio(request):
    projects = Projects.objects.order_by("-date").filter(display_online=True)
    categories = Category.objects.all()
    selected_tag = None
    return render(request, "portfolio/portfolio.html", {'projects': projects, 'categories': categories, 'selected_tag': selected_tag})

def category(request, category_slug ):
    category_obj = get_object_or_404(Category, slug=category_slug)
    projects = Projects.objects.order_by("-date").filter(display_online=True, categories=category_obj)
    categories = Category.objects.all()
    selected_tag = category_slug
    return render(request, "portfolio/portfolio.html", {'projects': projects, 'categories': categories, 'selected_tag': selected_tag})

def project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    if project.display_online:
        tag = request.GET.get('tag')
        return render(request, "portfolio/project.html", {'project': project, 'tag': tag})
    raise Http404("Error: project id not found")

def contact(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/contact.html", {'website_info': website_info})
