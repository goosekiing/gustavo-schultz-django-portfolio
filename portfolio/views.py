from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Count, Subquery, OuterRef
from portfolio.models import WebsiteInfo, CarouselImages, Projects, Category

PORTFOLIO_ORDER_OPTIONS = [
    ('Name | A - Z', 'name'),
    ('Published | New → Old', '-publish_date'),
    ('Published | Old → New', 'publish_date'),
    ('Developed | New → Old', '-develop_date'),
    ('Developed | Old → New', 'develop_date')
]

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
        'carousel_loops': carousel_loops,
    }
    return render(request, "portfolio/index.html", context)

def about(request):
    website_info = WebsiteInfo.objects.first()
    about_page = True
    context = {
        'website_info': website_info,
        'about_page': about_page
    }
    return render(request, "portfolio/about.html", context)

def portfolio(request, category_slug=None):
    website_info = WebsiteInfo.objects.first()
    selected_tag = None
    portfolio_page = True
    order_by = request.GET.get("order_by", "publish_date")

    if category_slug:
        category_obj = get_object_or_404(Category, slug=category_slug)
        projects = Projects.objects.order_by(order_by).filter(display_online=True, categories=category_obj)
        selected_tag = category_slug
    else:
        projects = Projects.objects.order_by(order_by).filter(display_online=True)

    categories = Category.objects.annotate(
        project_count=Count(
            Subquery(
                Projects.objects.filter(
                    categories=OuterRef('pk'),
                    display_online=True
                ).values('categories')
            )
        )
    ).filter(project_count__gt=0).order_by('name')
    
    context = {
        'website_info': website_info,
        'projects': projects,
        'categories': categories,
        'selected_tag': selected_tag,
        'portfolio_page': portfolio_page,
        'order_options': PORTFOLIO_ORDER_OPTIONS,
        'order_by': order_by,
    }
    return render(request, "portfolio/portfolio.html", context)

def project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    if project.display_online:
        tag = request.GET.get('tag')
        order_by = request.GET.get('order_by')
        display_carousel_buttons = True if project.images.count() > 1 else False
        portfolio_page = True
        context = {
            'project': project,
            'tag': tag,
            'display_carousel_buttons': display_carousel_buttons,
            'portfolio_page': portfolio_page,
            'order_by': order_by,
            }
        return render(request, "portfolio/project.html", context)
    raise Http404("Error: project id not found")

def contact(request):
    website_info = WebsiteInfo.objects.first()
    contact_page = True
    context = {
        'website_info': website_info,
        'contact_page': contact_page
    }
    return render(request, "portfolio/contact.html", context)
