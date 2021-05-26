# %%

import requests
import bs4
import datetime as dt

# %%

url = "https://en.wikipedia.org/wiki/Main_Page"
r = requests.get(url)
soup = bs4.BeautifulSoup(r.text, "html.parser")

# %%
itn = soup.find("div", {"id": "mp-itn"})
itn_list = itn.find("ul").find_all("li")
# %%
events = [{
    "text": x.text.replace(u'\xa0', u' ')
} for x in itn_list]
events
# %%
