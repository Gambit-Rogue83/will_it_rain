import os
import requests
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
OWM_ENDPOINT = os.environ.get("OWM_ENDPOINT")
account_sid = os.environ.get("TWILIO_ACCOUNT")
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




