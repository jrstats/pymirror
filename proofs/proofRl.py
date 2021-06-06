# %%

import requests
import bs4
import datetime
import re

# %%

url = "https://liquipedia.net/rocketleague/S-Tier_Tournaments"
r = requests.get(url)
soup = bs4.BeautifulSoup(r.text, "html.parser")
years = soup.find_all("div", {"class": "divTable table-full-width tournament-card"})
year_2021 = years[0]
# %%
events = [{
    "name": x.find("div", {"class": "divCell Tournament Header"}).text.strip(),
    "logo": x.find("span", {"class": "league-icon-small-image"}).find("img").get("src"),
    "date": x.find("div", {"class": "divCell EventDetails Date Header"}).text.strip(),
} for x in year_2021.find_all("div", {"class": "divRow"})]

for e in events:
    e["dateStr"] = e["date"]
    dates = re.search("^(\w{3}) (.*), (\d{4})", e["date"])
    datesList = str(dates.group(2)).split(" - ")
    if len(datesList) == 1:
        datesList.append(datesList[0])
    dateStr = f"{dates.group(1)} {{0}}, {dates.group(3)}"
    e["date"] = [datetime.datetime.strptime(dateStr.format(x), "%b %d, %Y") for x in range(int(datesList[0]), int(datesList[1])+1)]
    e["dateStart"] = min(e["date"])

eventsFuture = [e for e in events if max(e["date"]).date() >= datetime.date.today()]
eventsFuture.sort(key=lambda d: d["dateStart"])
print(eventsFuture)
# %%
