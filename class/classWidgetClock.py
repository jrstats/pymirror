import datetime
import logging
from classWidget import Widget
from classOrchestrator import Orchestrator


class WidgetClock(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, config: dict):
        super().__init__(widgetName, cronSyntax, priority, config)

    def update(self):
        now = datetime.datetime.now()
        date = now.strftime(self.config["dateFormat"])
        time = now.strftime(self.config["timeFormat"])
        output = f"""
        <h1>{time}</h1>
        <p>{date}</p>
        """
        
        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")
        
        return output

if __name__ == "__main__":
    wc = WidgetClock("w1", "* * * * *", 1, {})

    o = Orchestrator([wc])
    o.live()