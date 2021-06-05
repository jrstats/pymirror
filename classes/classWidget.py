import datetime
import logging

from crontab import CronTab
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
        self.widgetName: str = widgetName
        self.cronSyntax: str = cronSyntax
        self.priority: int = priority
        self.pane: str = pane
        self.slotNumber: int = slotNumber
        self.config: dict = config

        self.cron: CronTab = CronTab(self.cronSyntax)
        self.lastChecked = datetime.datetime.now()


    def getRefreshBoolean(self) -> bool:
        now: datetime.datetime = datetime.datetime.now()
        # logging.info(f"Most recent scheduled update for {self.widgetName} at {prevCron.strftime('%Y-%m-%d %H:%M:%S')}")

        ## if cron has occured between lastChecked and now
        if now.timestamp() + self.cron.previous(default_utc=False) > self.lastChecked.timestamp():
            output = True
        else:
            output = False

        self.lastChecked = now
        return output

    def update(self) -> None:
        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")


    def generateHtml(self) -> None:
        self.html: str = ""



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    cronSyntax = "* * * * * *"
    cronSyntax1 = "0 * * * * *"
    cron: croniter.croniter = croniter.croniter(cronSyntax, datetime.datetime.now())
    cron1: croniter.croniter = croniter.croniter(cronSyntax1, datetime.datetime.now())


    print(dir(cron.all_prev()), "\n")
    print(cron1.all_prev())


