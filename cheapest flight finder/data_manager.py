import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, endpoint_url):
        self.endpoint = endpoint_url


    def edit_row(self, row, str):
        data = {
            'price':{
                
                "iataCode": str,
                
            }
        }
        url = f"{self.endpoint}/{row}"
        print(url)
        return requests.put(url = url, json=data)
    

    def get_city_name(self,row):
        response = requests.get(url = f'{self.endpoint}/{row}')
        return response.json()['price']['city']