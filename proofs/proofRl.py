# %%

import requests
import bs4
import datetime as dt

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
events
# %%
