import datetime
import logging
import tkinter as tk
from classWidget import Widget
from classOrchestrator import Orchestrator


class WidgetClock(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, config: dict):
        super().__init__(widgetName, cronSyntax, priority, config)
        self.output = ('', '')

        ## initialise widget pane

    def update(self):
        now = datetime.datetime.now()
        date = now.strftime(self.config["dateFormat"])
        time = now.strftime(self.config["timeFormat"])
        self.output = (time, date)
        
        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def render(self):
        html = f"""
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