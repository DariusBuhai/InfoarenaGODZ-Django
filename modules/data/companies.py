import json

class DataCompanies():

    def get_companies():
        try:
            with open("data/companies.json", "r") as c:
                return json.loads(c.read())
        except Exception:
            return Exception

