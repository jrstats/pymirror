import datetime
import logging

class Widget():
    def __init__(self, widgetName, refreshRate):
        self.widgetName = widgetName
        self.refreshRate = refreshRate

    def update(self):
        print(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")