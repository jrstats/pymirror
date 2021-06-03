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

        # add widgets to the window
        for w in widgetList:
            self.window.addWidget(w)


    def getUpdateList(self) -> List[Widget]:
        ## assume update all widgets
        return [x for x in self.widgetList if x.getUpdateBoolean()]

    def updateList(self, updateList: List[Widget]) -> None:
        logging.info(f"updating {len(updateList)} widgets")
        for w in updateList:
            w.update()
        logging.info(f"successfully updated {len(updateList)} widgets")

    def renderList(self, updateList: List[Widget]) -> None:
        for w in updateList:
            logging.info(f"rendering {w.widgetName}")
            w.render()
        logging.info("finished rendering\n\n")

    def live(self) -> None:
        # initial load of all widgets
        self.updateList(self.widgetList)

        while True:
            ## Check for updates on every minute
            ## Could go in config file
            if datetime.datetime.now().microsecond == 0:
                # updateList: List[Widget] = self.getUpdateList()
                updateList = self.widgetList
                self.updateList(updateList)
                self.renderList(updateList)

                # render screen
                self.window.refresh() # NOT WORKING FOR SOME REASON

                # ## stop from re-running immediately
                if datetime.datetime.now().microsecond == 0:
                    time.sleep(1)



