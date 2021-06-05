import datetime
import tkinter as tk

from typing import Any, Tuple, Dict, Union
from .classWidget import Widget
from .classLogger import Logger
from .classSettings import Settings

logger = Logger(__name__, Settings.LOGGER)

class WidgetClock(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, pane: str, slotNumber: int, config: Dict[str, Any]) -> None:
        super().__init__(widgetName, cronSyntax, priority, pane, slotNumber, config)

    def update(self) -> None:
        now: datetime.datetime = datetime.datetime.now()
        date: str = now.strftime(self.config["dateFormat"])
        time: str = now.strftime(self.config["timeFormat"])
        self.output: Tuple[str, str] = (time, date)
        
        logger.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def generateHtml(self) -> None:
        logger.info(f"rendering {self.widgetName}")
        html: str = f"""
        <h1>{self.output[0]}</h1>
        <h4>{self.output[1]}</h4>
        """
        self.html: str = html
