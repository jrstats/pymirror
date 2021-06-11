import bs4
import datetime
import re
import requests

from typing import Dict, Any
from .classWidget import Widget
from .classLogger import Logger
from .classSettings import Settings

logger = Logger(__name__, Settings.LOGGER)


class WidgetRocketLeague(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, pane: str, slotNumber: int, config: Dict[str, Any]) -> None:
        super().__init__(widgetName, cronSyntax, priority, pane, slotNumber, config)

        # initialise class
        self.query: str = self.config["baseUrl"]


    def update(self) -> None:
        # load tournaments
        r: requests.Request = requests.get(self.query)
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.text, "html.parser")

        # parse data
        years = soup.find_all("div", {"class": "divTable table-full-width tournament-card"})
        latestYear = years[0]
        events = [{
            "name": x.find("div", {"class": "divCell Tournament Header"}).text.strip(),
            "logo": x.find("span", {"class": "league-icon-small-image"}).find("img").get("src"),
            "date": x.find("div", {"class": "divCell EventDetails Date Header"}).text.strip(),

        } for x in latestYear.find_all("div", {"class": "divRow"})]

        # format dates
        for e in events:
            e["dateStr"] = e["date"]
            dates = re.search("^(\w{3}) (.*), (\d{4})", e["date"])
            datesList = str(dates.group(2)).split(" - ")
            if len(datesList) == 1:
                datesList.append(datesList[0])
            dateStr = f"{dates.group(1)} {{0}}, {dates.group(3)}"
            e["date"] = [datetime.datetime.strptime(dateStr.format(x), "%b %d, %Y") for x in range(int(datesList[0]), int(datesList[1])+1)]
            e["dateStart"] = min(e["date"])

        # filter for future dates
        eventsFuture = [e for e in events if max(e["date"]).date() >= datetime.date.today()]
        eventsFuture.sort(key=lambda e: e["dateStart"])

        # set output
        self.output = eventsFuture
        logger.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def generateHtml(self) -> str:
        # render html with output data
        htmlList: List[str] = [f'<p>{x["name"]}: {x["dateStr"]}</p>' for x in self.output]
        html: str = self.listToHtml(htmlList)
        self.html: str = html


if __name__ == "__main__":
    config = {}
    wrl = WidgetRocketLeague(
        widgetName="rocketLeague",
        cronSyntax="0 * * * * * *",
        priority=1,
        config=Settings.ROCKET_LEAGUE,
        pane="right",
        slotNumber=2
    )
    wrl.update()
    print(wrl.generateHtml())
