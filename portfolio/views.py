from django.shortcuts import render
from django.http import Http404
from portfolio.models import WebsiteInfo, Projects

def index(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/index.html", {'website_info': website_info})

def about(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/about.html", {'website_info': website_info})

def portfolio(request):
    projects = Projects.objects.order_by("-date").filter(display_online=True)

    return render(request, "portfolio/portfolio.html", {'projects': projects})

def project(request, project_id):
    project = Projects.objects.get(pk=project_id)
    if project.display_online:
        return render(request, "portfolio/project.html", {'project': project})
    raise Http404("Error: project id not found")

def contact(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/contact.html", {'website_info': website_info})
