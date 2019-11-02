# Django Libraries
from django.http import HttpResponse
from django.http import JsonResponse
from newsapi import NewsApiClient

# Modules
from modules.news.news_sources import NewsFeed
from modules.data.companies import DataCompanies
from modules.news.news_classification import NewsFeedClassification
from modules.stocks.company_stocks import StockFeed

def index(request):

    newsapi = NewsApiClient(api_key='2fdb18e9297a437ab91a7ec7669bed35')
    try:
        sources = newsapi.get_sources()
    except Exception as e:
        return HttpResponse("Error: " + str(e))

    sources = newsapi.get_sources()
    print(sources)

    return JsonResponse(sources)

def get_companies(request):
    try:
        companies = DataCompanies.get_companies()
        return JsonResponse(companies, safe=False)
    except Exception as e:
        return HttpResponse("Error: " + str(e))

def get_news(request):
    try:
        news = NewsFeed.get_company_news('*')
        test = NewsFeed.get_twitter_news(' ')
        return JsonResponse(news)
    except Exception as e:
        return HttpResponse("Error: " + str(e))

def get_news_by_name(request, company):
    # Init
    try:
        news = NewsFeed.get_company_news(company)
        return JsonResponse(news)
    except Exception as e:
        return HttpResponse("Error: " + str(e))

def get_twitter_news_by_name(request, company):
    # Init
    try:
        news = NewsFeed.get_twitter_news(company)
        return JsonResponse(news, safe=False)
    except Exception as e:
        return HttpResponse("Error: " + str(e))

def get_classified_news_by_name(request, company):
    # Init
    try:
        NFC = NewsFeedClassification()

        news = NewsFeed.get_company_news(company)
        news = NFC.classify_news(news["articles"])
        return JsonResponse(news, safe=False)
    except Exception as e:
        return HttpResponse("Error: " + str(e))

def get_company_stocks(request, company):
    # Init
    try:
        SF = StockFeed()

        stocks = SF.get_company_stock(company)
        return JsonResponse(stocks)
    except Exception as e:
        return HttpResponse("Error: " + str(e))

