import datetime
import croniter
import logging

from typing import Dict, Union

class Widget():
    """
    Base Widget template.

    __init__():
        :param widgetName:
        :param cronSyntax: Minute, Hour, DayOfMonth, Month, DayOfWeek
        :param priority:
        :param config: 
    """
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, pane: str, slotNumber: int, config: Dict[str, Union[str, Dict]]) -> None:
        try:
            if not croniter.croniter.is_valid(cronSyntax):
                raise ValueError("cron syntax not valid")
        except AttributeError:
            raise TypeError("cronSyntax not of type str.")
        
        self.widgetName: str = widgetName
        self.cronSyntax: str = cronSyntax
        self.cron: croniter.croniter = croniter.croniter(self.cronSyntax)
        self.priority: int = priority
        self.pane: str = pane
        self.slotNumber: int = slotNumber
        self.config: dict = config



    def getUpdateBoolean(self) -> bool:
        now: datetime.datetime = datetime.datetime.now()
        c_prev: datetime.datetime = datetime.datetime.fromtimestamp(self.cron.get_prev())

        logging.info(f"Most recent scheduled update for {self.widgetName} at {c_prev.strftime('%Y-%m-%d %H:%M:%S')}")

        ## Assuming orchestrator refreshes every minute
        ## Could go in config file
        if now - c_prev < datetime.timedelta(minutes=1):
            logging.info(f"Updating {self.widgetName}...")
            return True
        else:
            return False

    def update(self) -> None:
        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")


    def render(self) -> str:
        pass



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    w1 = Widget("w1", "abc", 1, "left", 0, {})
    w1.getUpdateBoolean()



