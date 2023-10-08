import requests
import os
import pandas as pd
from itertools import chain
from dotenv import load_dotenv
from resources.sqlite import update_sql_widget
from widgets.tfl.helpers import convert_tfl_dates
from widgets.tfl.tfl_html import departures_html

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
load_dotenv(dotenv_path)
TFL_API_KEY = os.getenv("TFL_API_KEY")
TFL_STOP_POINT_IDS = os.getenv("TFL_STOP_POINT_IDS").split(",")

def update_tfl_departures():
    departures = [
        get_tfl_departures(station.split(":")[0], station.split(":")[1]) 
        for station in TFL_STOP_POINT_IDS
    ]
    departures_list = list(chain.from_iterable(departures))
    departures_df = transform_tfl_departures(departures_list)
    update_sql_widget("tfl_departures", departures_df, departures_html)


def get_tfl_departures(station_id, direction):
    # Define the URL to fetch departures
    url = f"https://api.tfl.gov.uk/StopPoint/{station_id}/Arrivals?app_key={TFL_API_KEY}"
    
    # Send the request and get the response
    response = requests.get(url)
    
    # Check if the request was successful (HTTP Status Code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Filter for eastbound departures and sort by expected arrival time
        departures = sorted(
            [d for d in data if d['direction'] == direction],
            key=lambda x: x['expectedArrival']
        )
        
        keys_to_keep = [
            "stationName",
            "destinationName",
            "lineName",
            "expectedArrival"
        ]
        departures = [
            {
                k: v
                for k, v in departure.items()
                if k in keys_to_keep
            }
            for departure in departures
        ]
        # Return the filtered and sorted departures
        return departures
    else:
        # Handle possible errors, such as API changes or network issues
        print(f"Failed to retrieve data: {response.status_code}")
        return response
    

def transform_tfl_departures(departures):
    df = (
        pd.DataFrame(departures)
        .assign(expectedArrivalLocal=lambda df: convert_tfl_dates(df["expectedArrival"]))
        .drop(["expectedArrival"], axis=1)
        .assign(stationName=lambda df: df["stationName"].str.replace(" Rail", "").str.replace(" Station", "").str.replace("London ", ""))
        .assign(destinationName=lambda df: df["destinationName"].str.replace(" Rail", "").str.replace(" Station", "").str.replace("London ", ""))
    )

    return df


if __name__ == "__main__":
    update_tfl_departures()