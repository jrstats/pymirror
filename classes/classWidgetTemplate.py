import datetime
import tkinter as tk
from typing import Dict, Any
from .classWidget import Widget
from .classLogger import Logger
from .classSettings import Settings

logger = Logger(__name__, Settings.LOGGER)


class WidgetTemplate(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, pane: str, slotNumber: int, config: Dict[str, Any]) -> None:
        super().__init__(widgetName, cronSyntax, priority, pane, slotNumber, config)

        # initialise class
        return None

    def update(self) -> None:
        # update output data

        logger.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def generateHtml(self) -> str:
        # render html with output data
        html: str = f"""

        """
        self.html: str = html


if __name__ == "__main__":
    config = {}
    wc = WidgetTemplate("w1", "* * * * *", 1, config)
    wc.update()
    print(wc.render())
