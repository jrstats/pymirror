import datetime
import json
import requests
import tkinter as tk
import urllib
from typing import List, Dict, Any
from .classWidget import Widget
from .classLogger import Logger
from .classSettings import Settings

logger = Logger(__name__, Settings.LOGGER)
class WidgetWeather(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, pane: str, slotNumber: int, config: Dict[str, Any]) -> None:
        super().__init__(widgetName, cronSyntax, priority, pane, slotNumber, config)


    def update(self) -> None:
        # set query url
        params: Dict[str, str] = {
            "lat": self.config["lat"],
            "lon": self.config["lon"],
            "exclude": self.config["exclude"],
            "appid": self.config["apiKey"],
            "units": self.config["units"]
        }
        query: str = self.config["baseUrl"] + urllib.parse.urlencode(params)

        # call API
        r: requests.Response = requests.get(query)
        weather: Dict[str, Any] = json.loads(r.text)

        # parse current weather
        currentWeather: Dict[str, Any] = {k: weather["current"][k] for k in self.config["desiredFields"]}

        self.output: Dict[str, Any] = currentWeather
        logger.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")


    def generateHtml(self) -> None:
        # render html with output data
        degrees: str = u"\u00b0"
        temperature: str = str(self.output["feels_like"])
        imgSource: str = self.config["imgUrl"].format(imgCode=self.output["weather"][0]["icon"])
        descriptionShort: str = self.output["weather"][0]["main"]
        descriptionLong: str = self.output["weather"][0]["description"]
        html: str = f"""
        <h1>{temperature}{degrees}C</h1>
        <img src="{imgSource}" width="50" height="50">
        <h3>{descriptionShort}</h3>
        <p>{descriptionLong}</p>
        """

        # Exception ignored in: <function PhotoImage.__del__ at 0x7f098d362940>
        # Traceback (most recent call last):
        # File "/usr/lib/python3/dist-packages/PIL/ImageTk.py", line 118, in __del__
        #     name = self.__photo.name
        # AttributeError: 'PhotoImage' object has no attribute '_PhotoImage__photo'


        self.html: str = html
        self.imageBase: str = imgSource.split("/")[0]
