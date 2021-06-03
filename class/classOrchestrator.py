import datetime
import logging
import time

from classWidget import Widget
from classWidgetClock import WidgetClock
from classWindow import Window

class Orchestrator():
    def __init__(self, widgetList: list[Widget]=[], window: Window=None) -> None:
        self.widgetList = widgetList
        self.window = window

        # add widgets to the window
        for w in widgetList:
            self.window.addWidget(w)


    def getUpdateList(self) -> list[Widget]:
        ## assume update all widgets
        return [x for x in self.widgetList if x.getUpdateBoolean()]

    def updateList(self, updateList: list[Widget]) -> None:
        logging.info(f"updating {len(updateList)} widgets")
        for w in updateList:
            w.update()
        logging.info(f"successfully updated {len(updateList)} widgets")

    def renderList(self, updateList: list[Widget]) -> None:
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
                # updateList: list[Widget] = self.getUpdateList()
                updateList = self.widgetList
                self.updateList(updateList)
                self.renderList(updateList)

                # render screen
                self.window.refresh()

                # ## stop from re-running immediately
                if datetime.datetime.now().microsecond == 0:
                    time.sleep(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    config = {
        "clock": {
            "dateFormat": "%Y-%m-%d",
            "timeFormat": "%H:%M:%S"
        },
        "bins": {
            "baseUrl": "https://www.ealing.gov.uk/site/custom_scripts/waste_collection/waste_collection.aspx",
            "postCode": "W5 2AR",
            "binsOfInterest": ["BLUE RECYCLING WHEELIE BIN", "FOOD BOX", "BLACK RUBBISH WHEELIE BIN"]
        },
        "rss": {
            "baseUrl": "https://www.reddit.com/user/m-xames/m/uk_politics/search.rss?",
            "searchTerms": {
                "q": "is_self:0 NOT site:(500px.com OR abload.de OR deviantart.com OR deviantart.net OR fav.me OR fbcdn.net OR flickr.com OR forgifs.com OR giphy.com OR gfycat.com OR gifsoup.com OR gyazo.com OR imageshack.us OR imgclean.com OR imgur.com OR instagr.am OR instagram.com OR mediacru.sh OR media.tumblr.com OR min.us OR minus.com OR myimghost.com OR photobucket.com OR picsarus.com OR puu.sh OR i.redd.it OR staticflickr.com OR tinypic.com OR twitpic.com)",
                "sort": "hot",
                "restrict_sr":1,
                "is_multi":1
            },
            "displayNumberOfItems": 3
        }
    }

    w1 = WidgetClock(
        widgetName="widget1", 
        cronSyntax="* * * * *", 
        priority=1, 
        config=config["clock"],
        pane="left",
        slotNumber=0)
    w2 = WidgetClock(
        widgetName="widget2", 
        cronSyntax="* * * * *", 
        priority=1, 
        config=config["clock"],
        pane="right",
        slotNumber=0)
    window = Window()

    o = Orchestrator([w1, w2], window)
    o.live()
