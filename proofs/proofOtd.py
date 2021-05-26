# %%

import requests
import bs4
import datetime as dt

# %%

url = "https://en.wikipedia.org/wiki/Main_Page"
r = requests.get(url)
soup = bs4.BeautifulSoup(r.text, "html.parser")

# %%
otd = soup.find("div", {"id": "mp-otd"})
otd_list = otd.find("ul").find_all("li")
# %%
events = [{
    "year": x.text.replace(u'\xa0', u' ').split(" – ")[0],
    "text": x.text.replace(u'\xa0', u' ').split(" – ")[1]
} for x in otd_list]
events
# %%
