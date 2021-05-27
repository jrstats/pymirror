import datetime
import croniter
import logging


class Widget():
    """
    Base Widget template.

    __init__():
        :param widgetName:
        :param cronSyntax: Minute, Hour, DayOfMonth, Month, DayOfWeek
        :param priority:
        :param params:
    """
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, params: dict):
        try:
            if not croniter.croniter.is_valid(cronSyntax):
                raise ValueError("cron syntax not valid")
        except AttributeError:
            raise TypeError("cronSyntax not of type str.")
        
        self.widgetName = widgetName
        self.cronSyntax = cronSyntax
        self.priority = priority
        self.params = params



    def getUpdateBoolean(self):
        c = croniter.croniter(self.cronSyntax)
        now = datetime.datetime.now()
        c_prev = datetime.datetime.fromtimestamp(c.get_prev())

        logging.info(f"Most recent scheduled update for {self.widgetName} at {c_prev.strftime('%Y-%m-%d %H:%M:%S')}")

        ## Assuming orchestrator refreshes every minute
        ## Could go in config file
        if now - c_prev < datetime.timedelta(minutes=1):
            logging.info(f"Updating {self.widgetName}...")
            return True
        else:
            return False

    def update(self):
        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    w1 = Widget("w1", "abc", 1, {})
    w1.getUpdateBoolean()



