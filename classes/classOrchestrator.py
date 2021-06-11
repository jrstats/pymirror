import datetime
import time

from math import floor
from typing import Dict, List, Any
from .classSettings import Settings
from .classLogger import Logger
from .classWidget import Widget
from .classWindow import Window

logger = Logger(__name__, Settings.LOGGER)
class Orchestrator():
    def __init__(self, widgetList: List[Widget], window: Window, config: Dict[str, Any]) -> None:
        self.widgetList: List[Widget] = widgetList
        self.window: Window = window
        self.config: Dict[str, Any] = config


    def checkOrcehstratorRefresh(self) -> bool:
        refreshDict = {
            "second": floor(datetime.datetime.now().microsecond/100000) == 0,
            "minute": datetime.datetime.now().second == 0,
        }

        return refreshDict[self.config["refresh"]]


    def getRefreshList(self) -> List[Widget]:
        ## assume update all widgets
        return [x for x in self.widgetList if x.getRefreshBoolean()]

    def refreshList(self, updateList: List[Widget]) -> None:
        logger.info(f"refreshing {len(updateList)} widgets")
        for w in updateList:
            logger.info(f"refreshing {w.widgetName}")
            w.update()
            w.generateHtml()
            self.window.loadWidget(w)
        logger.info(f"successfully updated {len(updateList)} widgets")

    def live(self) -> None:
        # initial load of all widgets
        self.refreshList(self.widgetList)
        for w in self.widgetList:
            self.window.loadWidget(w)


        while True:
            ## Check for updates on every minute
            ## Could go in config file
            if self.checkOrcehstratorRefresh():
                # updateList: List[Widget] = self.widgetList
                updateList: List[Widget] = self.getRefreshList()

                # render screen
                self.refreshList(updateList)
                self.window.refresh()

                # ## stop from re-running immediately
                while self.checkOrcehstratorRefresh():
                    time.sleep(0.1)



if __name__ == "__main__":
    pass
