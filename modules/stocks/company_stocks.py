import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

class StockFeed():

    def get_company_stock(company_smb):

        # Limited requests 500 due to demo app
        #URL = "https://www.alphavantage.co/query"
        #PARAMS = {'apikey': 'R1C0A37LIQEXRV8A',
                  #'function': 'TIME_SERIES_DAILY_ADJUSTED',
                  #'symbol': company_smb}
        #r = requests.get(url=URL, params=PARAMS)
        #r = r.json()

        with open("data/stocks.json", "r") as a:
            r = json.load(a)
            r = r[company_smb]

        try:
            times = []
            prices = []
            for x in r["Time Series (Daily)"]:
                times += [datetime.fromisoformat(x).timestamp()]
                prices += [float(r["Time Series (Daily)"][x]["1. open"])]

            # Show graph for debug only
            plt.plot(times, prices)
            plt.show()

            return {"times":times, "prices":prices}
        except Exception as e:
            print(str(e))

        return r


