import os
import requests
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
OWM_ENDPOINT = "5a7f8530d94fcfdfab59d3e126f8113faa7d4b9e"
account_sid = "7b0b352e142c62b7e426789bf9bf249afec58157"
auth_token = os.environ.get("AUTH_TOKEN")
PARAMETERS = {
    "lat": 47.606209,
    "lon": -122.332069,
    "appid": api_key,
    "cnt": 4,

}

response = requests.get(url=OWM_ENDPOINT, params=PARAMETERS)
response.raise_for_status()

data = response.json()

weather = data["list"]
will_rain = False

for hour_data in weather:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_="1501712261",
        to='+15558675310'
    )
    print(message.status)




