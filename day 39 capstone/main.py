#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import flight_search
import data_manager

cities = []
flights = []
endpoint = "https://api.sheety.co/8887817d3c2771a9c71be1314eb79cc9/flightDealFinder/prices"

data = data_manager.DataManager(endpoint)

response = data.edit_row(5, 'hello')
response.raise_for_status
print(response.text)

flight_data = flight_search.FlightSearch('https://api.tequila.kiwi.com/locations/query', 'Da62PYfGk3v2G7pthOOi-z0DvviFZXa5')

for i in range(2, 10):
    city = data.get_city_name(i)
    code = flight_data.getiata(city)
    cities.append(code)
    #data.edit_row(i, code)

print(len(cities))

flight_search_ = flight_search.FlightSearch('https://api.tequila.kiwi.com/v2/search', 'Da62PYfGk3v2G7pthOOi-z0DvviFZXa5')


for i in range(8):
    print(cities[i])
    data2 = flight_search_.get_flights('CVG', cities[i], '01/01/2025', '03/01/2025')
    flights.append(data2)

print(flights[1].json()['data'][0]['price'])

# come back and do this capstone project again please.