
# %%

import requests
import bs4

teams_of_interest = ["BRN"]
url = "https://www.espn.co.uk/football/fixtures?league=eng.2"
r = requests.get(url)
soup = bs4.BeautifulSoup(r.text, "html.parser")

# %%
schedule = soup.find("div", {"id": "sched-container"}).find("tbody")
rows = schedule.find_all("tr", {"class": "has-results"})
matches = [{
    "datetime": x.find("td", {"data-behavior": "date_time"}).get("data-date"),
    "homeTeam": {
        "name": x.find_all("a", {"class": "team-name"})[0].find("span").text,
        "abbr": x.find_all("a", {"class": "team-name"})[0].find("abbr").text,
        "logo": x.find_all("span", {"class": "team-logo"})[0].find("img").get("src")
    },
    "awayTeam": {
        "name": x.find_all("a", {"class": "team-name"})[1].find("span").text,
        "abbr": x.find_all("a", {"class": "team-name"})[1].find("abbr").text,
        "logo": x.find_all("span", {"class": "team-logo"})[1].find("img").get("src")
    },
} for x in rows]

matches_of_interest = [x for x in matches if (x["homeTeam"]["abbr"] in teams_of_interest) or (x["awayTeam"]["abbr"] in teams_of_interest)]
# %%
