import datetime

from crontab import CronTab
from typing import Dict, Union
from .classLogger import Logger
from .classSettings import Settings

logger = Logger(__name__, Settings.LOGGER)

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

        # https://github.com/josiahcarlson/parse-crontab
        self.cron: CronTab = CronTab(self.cronSyntax)
        self.lastChecked = datetime.datetime.now()


    def getRefreshBoolean(self) -> bool:
        now: datetime.datetime = datetime.datetime.now()
        # logger.info(f"Most recent scheduled update for {self.widgetName} at {prevCron.strftime('%Y-%m-%d %H:%M:%S')}")

        ## if cron has occured between lastChecked and now
        if now.timestamp() + self.cron.previous(default_utc=False) > self.lastChecked.timestamp():
            output = True
        else:
            output = False

        self.lastChecked = now
        return output

    def update(self) -> None:
        logger.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")


    def generateHtml(self) -> None:
        self.html: str = ""

