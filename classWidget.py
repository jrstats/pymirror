import datetime
import logging

class Widget():
    def __init__(self, widgetName, cronSyntax, priority, params):
        self.widgetName = widgetName
        self.cronSyntax = cronSyntax
        self.priority = priority
        self.params = params

    def update(self):
        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")