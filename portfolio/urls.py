from django.urls import path
from portfolio.views import index, portfolio

urlpatterns = [
    path('', index, name='index'),
    path('portfolio', portfolio, name="portfolio")
]