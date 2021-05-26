# %%

import requests
import bs4
import datetime as dt

# %%

url = "https://en.wikipedia.org/wiki/Main_Page"
r = requests.get(url)
soup = bs4.BeautifulSoup(r.text, "html.parser")

# %%
dyk = soup.find("div", {"id": "mp-dyk"})
dyk_list = dyk.find("ul").find_all("li")
# %%
events = [{
    "text": x.text.replace(u'\xa0', u' ')
} for x in dyk_list]
events
# %%
