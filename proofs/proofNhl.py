
# %%

import requests
import bs4

teams_of_interest = ["/nhl/teams/EDM/edmonton-oilers/"]
url = "https://www.cbssports.com/nhl/schedule/"
r = requests.get(url)
soup = bs4.BeautifulSoup(r.text, "html.parser")

# %%
match_date = soup.find("h4", {"class": "TableBase-title"}).text.strip()
schedule = soup.find("div", {"id": "TableBase"})
rows = schedule.find("tbody").find_all("tr")

matches = [{
    "datetime": match_date,
    "homeTeam": {
        "name": x.find_all("div", {"class": "TeamLogoNameLockup"})[0].find("div", {"class": "TeamLogoNameLockup-name"}).find("a").text,
        "abbr": x.find_all("div", {"class": "TeamLogoNameLockup"})[0].find("div", {"class": "TeamLogoNameLockup-name"}).find("a").get("href"),
        "logo": x.find_all("div", {"class": "TeamLogoNameLockup"})[0].find("div", {"class": "TeamLogoNameLockup-logo"}).find("img").get("data-lazy")
    },
    "awayTeam": {
        "name": x.find_all("div", {"class": "TeamLogoNameLockup"})[1].find("div", {"class": "TeamLogoNameLockup-name"}).find("a").text,
        "abbr": x.find_all("div", {"class": "TeamLogoNameLockup"})[1].find("div", {"class": "TeamLogoNameLockup-name"}).find("a").get("href"),
        "logo": x.find_all("div", {"class": "TeamLogoNameLockup"})[1].find("div", {"class": "TeamLogoNameLockup-logo"}).find("img").get("data-lazy")
    },
} for x in rows]

matches_of_interest = [x for x in matches if (x["homeTeam"]["abbr"] in teams_of_interest) or (x["awayTeam"]["abbr"] in teams_of_interest)]
# %%
