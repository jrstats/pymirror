import datetime
import feedparser
import logging
import tkinter as tk
import urllib
from classWidget import Widget
from classOrchestrator import Orchestrator


class WidgetRss(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, config: dict) -> None:
        super().__init__(widgetName, cronSyntax, priority, config)

        # initialise class
        self.output = None
        self.query = self.config["baseUrl"] + urllib.parse.urlencode(config["searchTerms"])


    def update(self) -> None:
        # update output data
        feed = feedparser.parse(self.query)
        self.output: list = feed.entries

        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def render(self) -> str:
        # render html with output data
        htmlList: list = [x["title"] for x in self.output][:self.config["displayNumberOfItems"]]
        html = "<ul><li>"
        html += "</li>\n<li>".join(htmlList)
        html += "</li></ul>"
        return html

if __name__ == "__main__":
    config = {
        "baseUrl": "https://www.reddit.com/user/m-xames/m/uk_politics/search.rss?",
        "searchTerms": {
            "q": "is_self:0 NOT site:(500px.com OR abload.de OR deviantart.com OR deviantart.net OR fav.me OR fbcdn.net OR flickr.com OR forgifs.com OR giphy.com OR gfycat.com OR gifsoup.com OR gyazo.com OR imageshack.us OR imgclean.com OR imgur.com OR instagr.am OR instagram.com OR mediacru.sh OR media.tumblr.com OR min.us OR minus.com OR myimghost.com OR photobucket.com OR picsarus.com OR puu.sh OR i.redd.it OR staticflickr.com OR tinypic.com OR twitpic.com)",
            "sort": "hot",
            "restrict_sr":1,
            "is_multi":1
        },
        "displayNumberOfItems": 3
    }

    wc = WidgetRss("w1", "* * * * *", 1, config)
    wc.update()
    print(wc.render())