from modules.news.news_sources import NewsFeed
import json
from modules.classifiers.h1_classifier import H1CLASSIFIER

class NewsFeedClassification():

    def classify_news_by_company(company):
        return 0

    def classify_news(self, news):

        index = 0
        for new in news:
            PN = H1CLASSIFIER(new["title"], new["description"], new["content"])
            news[index]["Score"] = PN.get_hash1()
            index+=1

        return news

    def classify_news_by_stock(self, news, stocks):

        index = 0
        for new in news:
            PN = H1CLASSIFIER(new["title"], new["description"], new["content"])
            news[index]["Score"] = PN.get_hash1()
            index += 1



