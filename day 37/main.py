import requests
import datetime

TOKEN = "jbvhdbfkhb2esyg03biy"
USERNAME = 'abhii'

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
#response = requests.post(url=pixela_endpoint,json=user_params)

#print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

today = datetime.datetime(year=2024, month=3, day=20)

today = today.strftime('%Y%m%d')

response=requests.post(url=graph_endpoint, json=graph_config, headers = headers)
print(response.text)

post_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'

post_details = {
    'date': today,
    'quantity': '10.5'
}

response=requests.post(url=post_endpoint, json=post_details, headers = headers)
print(response.text)