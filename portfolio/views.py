from django.shortcuts import render
from portfolio.models import Projects

def index(request):
    return render(request, "portfolio/index.html")

def portfolio(request):
    projects = Projects.objects.order_by("-date")

    return render(request, "portfolio/portfolio.html", {'projects': projects})

def project(request, project_id):
    project = Projects.objects.get(pk=project_id)
    return render(request, "portfolio/project.html", {'project': project})
