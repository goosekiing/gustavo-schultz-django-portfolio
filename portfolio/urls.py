from django.urls import path
from portfolio.views import index, about, portfolio, project, contact

urlpatterns = [
    path('', index, name='index'),
    path("about/", about, name="about"),
    path('portfolio/', portfolio, name="portfolio"),
    path('portfolio/<slug:category_slug>', portfolio, name='category'),
    path('portfolio/<int:project_id>/', project, name='project'),
    path('contact', contact, name='contact'),
]
