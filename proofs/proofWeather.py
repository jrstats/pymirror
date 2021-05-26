
# %%
import urllib
import requests
import json
import datetime as dt

api_key = "5a8b46aca98892acfb9111c0cf581cb0"
lat = "51.5149"
lon = "0.3019"
desired_fields = ["dt", "feels_like", "weather"]
date_format = ""

base_url = "https://api.openweathermap.org/data/2.5/onecall?"
params = {
    "lat": lat,
    "lon": lon,
    "exclude": "minutely,hourly",
    "appid": api_key,
    "units": "metric",
}

query = base_url + urllib.parse.urlencode(params)

# %%
r = requests.get(query)
weather = json.loads(r.text)
# %%

current_weather = {k: weather["current"][k] for k in desired_fields}
current_weather["date"] = dt.datetime.fromtimestamp(current_weather["dt"])
del current_weather["dt"]

# %%
daily_weather = [{k: x[k] for k in desired_fields} for x in weather["daily"]]

# %%
