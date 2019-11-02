import requests

class StockFeed():

    def get_company_stock(company_smb):
        URL = "https://www.alphavantage.co/query"

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'apikey': 'R1C0A37LIQEXRV8A',
                  'function': 'TIME_SERIES_DAILY_ADJUSTED',
                  'symbol': company_smb}

        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)

        return r.json()


