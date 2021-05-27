from uk_covid19 import Cov19API

england_only = [
    'areaType=nation',
    'areaName=England'
]

cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeaths28DaysByDeathDate": "newDeaths28DaysByDeathDate",
    "cumDeaths28DaysByDeathDate": "cumDeaths28DaysByDeathDate"
}

api = Cov19API(filters=england_only, structure=cases_and_deaths)
data = api.get_json()

print(data)