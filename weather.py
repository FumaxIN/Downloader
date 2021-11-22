import json
import requests
# import logging
from urllib.request import urlopen
# from urllib.error import URLError, HTTPError

api_key = "61c567d010c515a50bf6f9f49fce9e3d"
city_name = "Ramnagar"
state_code = "110003"

full_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key
print(full_url)

with urlopen(full_url) as weather:
    data = weather.read()

result = json.loads(data)
print(json.dumps(result, indent=2))
print("\nLonitude = ", json.dumps(result["coord"]["lon"], indent=2))
