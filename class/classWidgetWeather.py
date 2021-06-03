import datetime
import logging
import tkinter as tk
from typing import Dict, Any
from .classWidget import Widget


class WidgetWeather(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, pane: str, slotNumber: int, config: Dict[str, Any]) -> None:
        super().__init__(widgetName, cronSyntax, priority, pane, slotNumber, config)

        # initialise class
        self.output = None


    def update(self) -> None:
        # update output data

        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def render(self) -> str:
        # render html with output data
        html: str = f"""

        """
        return html

if __name__ == "__main__":
    config = {}
    wc = WidgetWeather("w1", "* * * * *", 1, config)
    wc.update()
    print(wc.render())