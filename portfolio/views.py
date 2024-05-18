from django.shortcuts import render
from portfolio.models import About, Projects, Contact

def index(request):
    return render(request, "portfolio/index.html")

def about(request):
    about_info = About.objects.first()
    return render(request, "portfolio/about.html", {'about_info': about_info})

def portfolio(request):
    projects = Projects.objects.order_by("-date")

    return render(request, "portfolio/portfolio.html", {'projects': projects})

def project(request, project_id):
    project = Projects.objects.get(pk=project_id)
    return render(request, "portfolio/project.html", {'project': project})

def contact(request):
    contact_info = Contact.objects.first()
    return render(request, "portfolio/contact.html", {'contact_info': contact_info})
