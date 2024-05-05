import requests
from twilio.rest import Client

api_key = "6add9cc4f2e0549f53281315c849d970"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC7c357bb2c70d78979800071781270f39"
auth_token = "0549b71f9a1e07f77368c2e0bac53485"
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

# weather_code = [data["list"][num]["weather"][0]["id"] for num in range(3)]



# weather = data["list"]
# print(weather)
# twelve_hour_rain = {data["list"]["weather"]["id"]: value, for (key, value) in data if id < 700}


