# https://github.com/nwootton/MMM-UKNationalRail
# https://www.nationalrail.co.uk/100296.aspx
# http://lite.realtime.nationalrail.co.uk/openldbws/
# https://www.nationalrail.co.uk/stations_destinations/48541.aspx
# https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2017-10-01
# https://github.com/grundleborg/nrewebservices

# This file contains an example of how to make a very basic use of this library to query all the
# departures at a station using the LDBWS API. For more detailed information on how to use this
# library, and all the web services, API endpoints and objects and properties that you can use
# with this library, please see the API docs at http://nrewebservices.readthedocs.org

####################################################################################################
# Load the configuration.

# Set up the address for the LDBWS server.
API_URL = "https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2017-10-01"
API_KEY = "fdbdc556-f184-414a-ae83-b98d6ae2dcf0"

####################################################################################################
# An example of getting a regular departure board.

# Import the ldbws session class.
from nrewebservices.ldbws import Session

# Instantiate the web service session.
session = Session(API_URL, API_KEY)

# Get a departure board containing the next ten departures from Reading.
board = session.get_station_board("WEA", rows=50, include_departures=True, include_arrivals=False)

print("The next 50 departures from {} are:".format(board.location_name))

# Loop over all the train services in that board.
for service in board.train_services:
    
    # Print some basic information about that train service.
    print("    {} to {}: due {}.".format(
        service.std,
        service.destination,
        service.etd
    ))

print()

####################################################################################################
# An example of getting the Next Departures to various locations board.

# Import the ldbws session class.
from nrewebservices.ldbws import Session

# Instantiate the web service session.
session = Session(API_URL, API_KEY)

# Get a the next departures from Reading to Paddington and Oxford.
board = session.get_next_departures("WEA", ["PAD"])

print("The next departures from {} to popular destinations are as follows:".format(board.location_name))

# Loop over the departures.
for departure in board.next_departures:

    print("To {}:".format(departure.crs))

    # Build a list of destinations for each train service.
    destinations = [destination.location_name for destination in departure.service.destinations]

    # Print some basic information about that train service.
    print("    {} to {}: due {}.".format(
        departure.service.std,
        ",".join(destinations),
        departure.service.etd
    ))

print()
# %%
