import requests


class Weather:

    def __init__(self):
        city = "New Orleans"
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q":city}
        headers = {
            "X-RapidAPI-Key": "9b3e089dfdmsh441fc6b319431ddp14ec82jsn1f9a66bcec21",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        self.condition = response.json()['current']['condition']['text']
        self.precipitation = response.json()['current']['precip_in']

        self.delay = float((self.precipitation//5)*300)
