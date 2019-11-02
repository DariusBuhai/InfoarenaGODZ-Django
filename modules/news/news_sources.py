from newsapi import NewsApiClient
import requests

API_KEY = '2fdb18e9297a437ab91a7ec7669bed35'
newsapi = NewsApiClient(api_key=API_KEY)

class NewsFeed():

    def get_company_news(company = ""):

        URL = "https://newsapi.org/v2/everything"

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'apiKey': '2fdb18e9297a437ab91a7ec7669bed35',
                  'q' : company,
                  'sortBy':'popularity'}

        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)

        # extracting data in json format
        data = r.json()
        return data