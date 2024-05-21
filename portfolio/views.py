from django.shortcuts import render
from portfolio.models import WebsiteInfo, Projects

def index(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/index.html", {'website_info': website_info})

def about(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/about.html", {'website_info': website_info})

def portfolio(request):
    projects = Projects.objects.order_by("-date")

    return render(request, "portfolio/portfolio.html", {'projects': projects})

def project(request, project_id):
    project = Projects.objects.get(pk=project_id)
    return render(request, "portfolio/project.html", {'project': project})

def contact(request):
    website_info = WebsiteInfo.objects.first()
    return render(request, "portfolio/contact.html", {'website_info': website_info})
