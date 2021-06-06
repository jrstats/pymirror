import datetime
import feedparser
import tkinter as tk
import urllib.parse
from typing import List, Dict, Any
from .classWidget import Widget
from .classLogger import Logger
from .classSettings import Settings

logger = Logger(__name__, Settings.LOGGER)


class WidgetRss(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, pane: str, slotNumber: int, config: Dict[str, Any]) -> None:
        super().__init__(widgetName, cronSyntax, priority, pane, slotNumber, config)

        # initialise class
        self.query: str = self.config["baseUrl"] + urllib.parse.urlencode(config["searchTerms"])


    def update(self) -> None:
        # update output data
        feed = feedparser.parse(self.query)
        self.output: List = feed.entries

        logger.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def generateHtml(self) -> None:
        # render html with output data
        htmlList: list = [x["title"] for x in self.output][:self.config["displayNumberOfItems"]]
        html: str = self.listToHtml(htmlList)

        self.html: str = html
