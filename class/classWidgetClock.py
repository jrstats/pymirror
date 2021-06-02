import datetime
import logging
import tkinter as tk
from classWidget import Widget
from classOrchestrator import Orchestrator


class WidgetClock(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, config: dict) -> None:
        super().__init__(widgetName, cronSyntax, priority, config)
        self.output = ('', '')

        ## initialise widget pane

    def update(self) -> None:
        now: datetime.datetime = datetime.datetime.now()
        date: str = now.strftime(self.config["dateFormat"])
        time: str = now.strftime(self.config["timeFormat"])
        self.output: tuple = (time, date)
        
        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def render(self) -> str:
        html: str = f"""
        <h1>{self.output[0]}</h1>
        <h4>{self.output[1]}</h4>
        """
        return html

if __name__ == "__main__":
    config = {
        "dateFormat": "%Y-%m-%d",
        "timeFormat": "%H:%M:%S"
    }
    wc = WidgetClock("w1", "* * * * *", 1, config)
    wc.update()
    print(wc.render())