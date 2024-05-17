import requests
from datetime import datetime

MYLONG = 120.960518
MYLAT = 23.697809

response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()
isslat = float(data['iss_position']['latitude'])
isslong = float(data['iss_position']['longitude'])

print(data)

parameters = {
    'lat': MYLAT,
    'lng': MYLONG,
    'formatted': 0
}
response = requests.get('https://api.sunrise-sunset.org/json', params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(":")[0]
sunset = data['results']['sunset'].split('T')[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)

# do the rest onyour own