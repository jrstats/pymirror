import classWidget
import datetime
import logging
import time


class Orchestrator():
    def __init__(self, widgetList=[]):
        self.widgetList = widgetList

    def getUpdateList(self):
        ## assume update all widgets
        return self.widgetList

    def updateList(self, updateList):
        logging.info(f"updating {len(updateList)} widgets")
        for w in updateList:
            w.update()
        logging.info(f"successfully updated {len(updateList)} widgets\n\n")

    def live(self):
        o.updateList(self.widgetList)

        while True:
            ## check for updates on every minute
            if datetime.datetime.now().second == 0:
                updateList = self.getUpdateList()
                o.updateList(updateList)

                ## stop from re-running immediately
                if datetime.datetime.now().second == 0:
                    time.sleep(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    w1 = classWidget.Widget("widget1", 1)
    w2 = classWidget.Widget("widget2", 2)

    o = Orchestrator([w1, w2])
    o.live()
