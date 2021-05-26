# https://github.com/ryck/MMM-TFL-Arrivals
# get /StopPoint/Meta/Modes 
# get /StopPoint/Mode/{modes}
# get /Line/{id}/Timetable/{fromStopPointId} 
# get /Line/{ids}/Disruption
# get /Line/Search/{query} 
# get /Line/Mode/{modes}

# %%
import json
import requests
import urllib

base_url = "https://api.tfl.gov.uk"
params = {}

modes_endpoint = "StopPoint/Meta/Modes"
r_modes = requests.get(f"{base_url}/{modes_endpoint}?{urllib.parse.urlencode(params)}")
all_modes = [x["modeName"] for x in json.loads(r_modes.text)]
# %%
stoppoints_endpoint = "/StopPoint/Mode/{modes}".format(modes="cable-car")
r_stoppoints = requests.get(f"{base_url}/{stoppoints_endpoint}?{urllib.parse.urlencode(params)}")
all_stops = [{
    "naptanId": x["naptanId"],
    "modes": x["modes"],
    "stopType": x["stopType"],
    # "stationNaptan": x["stationNaptan"],
    "commonName": x["commonName"],
} for x in json.loads(r_stoppoints.text)["stopPoints"]]
# %%
