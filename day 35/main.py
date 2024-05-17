import requests
import smtplib

my_email = "abhtecho@gmail.com"
password = "zdfe wjll blym bbeb"

will_rain = False

api_key = 'b363b30ef8e7a84368df8660643447c9'
parameters = {
    'lat': 25.105497,
    'lon': 120.9605,
    'appid': api_key,
    'cnt': 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params = parameters)

response.raise_for_status()

data = response.json()
for i in range(4):
    
    code = data['list'][i]['weather'][0]['id']
    if int(code) < 700:
        will_rain = True

if will_rain:
    message = "Subject: Rain Alert\n\nHello darling its gonna rain today, carry your umbrella love :)"
else:
    message = "Subject: No signs of Rain\n\nHello darling its not gonna rain, have a sweet sunny day my beautiful princess <3"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user = my_email, password = password)
connection.sendmail(from_addr = my_email, to_addrs = "hesaree123@gmail.com", msg = message)
connection.close()



 