import classWidget
import time

class Orchestrator():
    def __init__(self, widgetList=[]):
        self.widgetList = widgetList

    def getUpdateList(self):
        ## assume update all widgets
        return self.widgetList

    def updateList(self, updateList):
        for w in updateList:
            w.update()

    def live(self):
        while True:
            updateList = self.getUpdateList()
            o.updateList(updateList)
            time.sleep(1)


if __name__ == "__main__":
    w1 = classWidget.Widget("widget1", 1)
    w2 = classWidget.Widget("widget2", 2)

    o = Orchestrator([w1, w2])
    o.live()
