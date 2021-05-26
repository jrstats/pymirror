# https://github.com/ryck/MMM-TFL-Arrivals
# get /StopPoint/Meta/Modes 
# get /StopPoint/Mode/{modes}
# get /Line/Mode/{modes}
# get /Line/{id}/StopPoints
# get /Line/{ids}/Arrivals/{stopPointId}[?direction][&destinationStationId]
# get /Line/{ids}/Disruption
# get /Line/Search/{query} 

# %%
import json
import requests
import urllib

base_url = "https://api.tfl.gov.uk"
params = {}

# modes
modes_endpoint = "/StopPoint/Meta/Modes"
r_modes = requests.get(f"{base_url}{modes_endpoint}?{urllib.parse.urlencode(params)}")
all_modes = [x["modeName"] for x in json.loads(r_modes.text)]
# %%
test_mode = "bus"


# %%

# lines
lines_endpoint = "/Line/Mode/{modes}".format(modes=test_mode)
r_lines = requests.get(f"{base_url}{lines_endpoint}?{urllib.parse.urlencode(params)}")

line_id = [x["id"] for x in json.loads(r_lines.text)][0]

# %%
# stoppoints
stoppoints_endpoint = "/Line/{id}/StopPoints".format(id=line_id)
r_stoppoints = requests.get(f"{base_url}/{stoppoints_endpoint}?{urllib.parse.urlencode(params)}")
all_stops = [{
    "naptanId": x["naptanId"],
    "modes": x["modes"],
    "stopType": x["stopType"],
    # "stationNaptan": x["stationNaptan"],
    "commonName": x["commonName"],
} for x in json.loads(r_stoppoints.text)]

# %%

# arrivals
naptan_id = "490007086B" #"490G00018892"
arrivals_endpoint = "/Line/{ids}/Arrivals/{stopPointId}".format(ids=line_id, stopPointId=naptan_id)
query_url = f"{base_url}{arrivals_endpoint}?{urllib.parse.urlencode(params)}"
r_arrivals = requests.get(query_url)

all_arrivals = [{
    "stationName": x["stationName"],
    "lineName": x["lineName"],
    "platformName": x["platformName"],
    "destinationName": x["destinationName"],
    "expectedArrival": x["expectedArrival"]
} for x in json.loads(r_arrivals.text)]
# %%
# r = requests.get("https://api.tfl.gov.uk/Line/1/Arrivals/")
all_arrivals
# %%
