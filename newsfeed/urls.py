from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.get_news, name='get_news'),
    path('companies/', views.get_companies, name='get_companies'),
    path('classified_news/<slug:company>', views.get_classified_news_by_name, name='get_classified_news_by_name'),
    path('news/<slug:company>', views.get_news_by_name, name='get_news_by_name'),
    path('tweets/<slug:company>', views.get_twitter_news_by_name, name='get_twitter_news_by_name'),
    path('stocks/<slug:company>', views.get_company_stocks, name='get_company_stocks'),
]