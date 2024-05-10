from django.shortcuts import render
from portfolio.models import Projects

def index(request):
    projects = Projects.objects.order_by("-date")

    return render(request, "portfolio/index.html", {'projects': projects})
