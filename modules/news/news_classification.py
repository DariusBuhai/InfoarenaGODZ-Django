from modules.news.news_sources import NewsFeed
import json

class NewsFeedClassification():

    def classify_news_by_company(company):
        return 0

    def classify_news(news):

        with open("data/words_analysis.json", "r") as c:
            words_analysis = json.loads(c.read())


        return news
        #for current in news:


