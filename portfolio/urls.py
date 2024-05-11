from django.urls import path
from portfolio.views import index, portfolio, project

urlpatterns = [
    path('', index, name='index'),
    path('portfolio/', portfolio, name="portfolio"),
    path('project/<int:project_id>/', project, name='project')
]