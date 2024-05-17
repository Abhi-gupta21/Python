import data_manager
import requests


class FlightSearch:
    def __init__(self, endpoint, api):
        self.endpoint = endpoint
        self.api = api
    
    def getiata(self, city):
        params = {
            "term": city
        }

        header = {
            "apikey": self.api
        }

        response = requests.get(url = self.endpoint, params=params, headers = header)
        data=response.json()
        return data['locations'][0]['code']
    
    def get_flights(self, fly_from, fly_to, date_from, date_to):
        
        header = {
            "apikey": self.api
        }

        params = {
            'fly_from': fly_from,
            'fly_to': fly_to,
            'date_from': date_from,
            'date_to': date_to
        }
        
        response = requests.get(url = self.endpoint, headers = header, params = params)

        return response