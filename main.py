import logging
from classes.classWidgetClock import WidgetClock
from classes.classWindow import Window
from classes.classOrchestrator import Orchestrator

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    configClock = {
        "dateFormat": "%Y-%m-%d",
        "timeFormat": "%H:%M:%S"}
    configBins = {
        "baseUrl": "https://www.ealing.gov.uk/site/custom_scripts/waste_collection/waste_collection.aspx",
        "postCode": "W5 2AR",
        "binsOfInterest": ["BLUE RECYCLING WHEELIE BIN", "FOOD BOX", "BLACK RUBBISH WHEELIE BIN"]}
    configRss = {
        "baseUrl": "https://www.reddit.com/user/m-xames/m/uk_politics/search.rss?",
        "searchTerms": {
            "q": "is_self:0 NOT site:(500px.com OR abload.de OR deviantart.com OR deviantart.net OR fav.me OR fbcdn.net OR flickr.com OR forgifs.com OR giphy.com OR gfycat.com OR gifsoup.com OR gyazo.com OR imageshack.us OR imgclean.com OR imgur.com OR instagr.am OR instagram.com OR mediacru.sh OR media.tumblr.com OR min.us OR minus.com OR myimghost.com OR photobucket.com OR picsarus.com OR puu.sh OR i.redd.it OR staticflickr.com OR tinypic.com OR twitpic.com)",
            "sort": "hot",
            "restrict_sr":1,
            "is_multi":1},
        "displayNumberOfItems": 3}

    w1 = WidgetClock(
        widgetName="widget1", 
        cronSyntax="* * * * *", 
        priority=1, 
        config=configClock,
        pane="left",
        slotNumber=0)
    w2 = WidgetClock(
        widgetName="widget2", 
        cronSyntax="* * * * *", 
        priority=1, 
        config=configClock,
        pane="right",
        slotNumber=0)
    window = Window()

    o = Orchestrator([w1, w2], window)
    o.live()