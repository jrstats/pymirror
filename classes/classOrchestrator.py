import datetime
import logging
import time

from typing import List
from .classWidget import Widget
from .classWindow import Window

class Orchestrator():
    def __init__(self, widgetList: List[Widget], window: Window) -> None:
        self.widgetList: List[Widget] = widgetList
        self.window: Window = window




    def getRefreshList(self) -> List[Widget]:
        ## assume update all widgets
        return [x for x in self.widgetList if x.getRefreshBoolean()]

    def refreshList(self, updateList: List[Widget]) -> None:
        logging.info(f"refreshing {len(updateList)} widgets")
        for w in updateList:
            logging.info(f"refreshing {w.widgetName}")
            w.update()
            w.generateHtml()
            self.window.loadWidget(w)
        logging.info(f"successfully updated {len(updateList)} widgets")

    def live(self) -> None:
        # initial load of all widgets
        self.refreshList(self.widgetList)
        for w in self.widgetList:
            self.window.loadWidget(w)


        while True:
            ## Check for updates on every minute
            ## Could go in config file
            if datetime.datetime.now().microsecond == 0:
                # updateList: List[Widget] = self.widgetList
                updateList: List[Widget] = self.getRefreshList()

                # render screen
                self.refreshList(updateList)
                self.window.refresh()

                # ## stop from re-running immediately
                if datetime.datetime.now().microsecond == 0:
                    time.sleep(1)



if __name__ == "__main__":
    pass
