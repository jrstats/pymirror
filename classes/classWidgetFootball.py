import bs4
import datetime
import requests
import tkinter as tk
from typing import Dict, Any, List
from .classWidget import Widget
from .classLogger import Logger
from .classSettings import Settings

logger = Logger(__name__, Settings.LOGGER)
class WidgetFootball(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, pane: str, slotNumber: int, config: Dict[str, Any]) -> None:
        super().__init__(widgetName, cronSyntax, priority, pane, slotNumber, config)

        # initialise class
        self.output = None


    def update(self) -> None:
        # load football matches
        url = self.config["baseUrl"] + "?league=" + self.config["league"]
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, "html.parser")

        # parse results
        schedule = soup.find("div", {"id": "sched-container"}).find("tbody")
        rows = schedule.find_all("tr", {"class": "has-results"})
        matches = [{
            # "datetime": x.find("td", {"data-behavior": "date_time"}).get("data-date"),
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
        matchesOfInterest = [x for x in matches if (x["homeTeam"]["abbr"] in self.config["teamsOfInterest"]) or (x["awayTeam"]["abbr"] in self.config["teamsOfInterest"])]

        ## TODO: if matchdate < today, etc.

        self.output = matchesOfInterest
        logger.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def generateHtml(self) -> str:
        # render html with output data
        # TODO: improve html
        htmlList: List[str] = [f'<p>{x["homeTeam"]["name"]} vs. {x["awayTeam"]["name"]}</p>' for x in self.output]
        html = "<ul><li>"
        html += "</li>\n<li>".join(htmlList)
        html += "</li></ul>"

        self.html: str = html

if __name__ == "__main__":
    config = {}
    wc = WidgetTemplate("w1", "* * * * *", 1, config)
    wc.update()
    print(wc.render())
