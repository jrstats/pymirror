import math
import screeninfo
import tkinter as tk
import tkinterweb as tkw
import logging

from typing import List
from .classWidget import Widget
from .classWidgetBins import WidgetBins
from .classWidgetClock import WidgetClock
from .classWidgetRss import WidgetRss


class Window():
    def __init__(self, widgetSize: int=200) -> None:
        self.widgetSize: int = widgetSize
        self.monitors: List[screeninfo.Monitor] = screeninfo.get_monitors()
        m: screeninfo.Monitor = self.monitors[0]
        

        # root page
        self.root: tk.Tk = tk.Tk()
        self.root.geometry(f"{m.width}x{m.height}+{m.x}+{m.y}")
        # 1440x900+0+0

        # add left and right pane
        self.leftPane: tk.Frame = tk.Frame(self.root, background="#000000", width=self.widgetSize, height=m.height)
        self.rightPane: tk.Frame = tk.Frame(self.root, background="#000000", width=self.widgetSize, height=m.height)
        self.centrePane: tk.Frame = tk.Frame(self.root, background="#ffffff", width=m.width-(2*self.widgetSize))
        self.leftPane.pack(side="left", fill="x")
        self.rightPane.pack(side="right", fill="x")
        self.centrePane.pack(side="top", fill="both", expand=True)

        # calculate number of slots
        widgetsTall: int = math.floor(m.height/self.widgetSize)
        self.paddingY: float = (m.width - widgetsTall*self.widgetSize)/(2*(self.widgetSize + 1))
        self.widgetWidth: int = self.widgetSize
        self.widgetHeight: float = self.widgetSize + 2*self.paddingY
        
        # split panes into widget slots
        self.leftFrames: List[tkw.HtmlLabel] = [tk.Frame(self.leftPane, width=self.widgetWidth, height=self.widgetHeight, bg="black") for i in range(widgetsTall)]
        self.rightFrames: List[tkw.HtmlLabel] = [tk.Frame(self.rightPane, width=self.widgetWidth, height=self.widgetHeight, bg="black") for i in range(widgetsTall)]
        self.leftWidgets: List[tkw.HtmlLabel] = [tkw.HtmlLabel(i, "<p>Empty widget</p><hr>", width=self.widgetWidth, height=self.widgetHeight) for i in self.leftFrames]
        self.rightWidgets: List[tkw.HtmlLabel] = [tkw.HtmlLabel(i, "<p>Empty widget</p><hr>", width=self.widgetWidth, height=self.widgetHeight) for i in self.rightFrames]
        

        # css template
        self.bodyCss: str = """
        body {
            background-color: black;
            color: white
        }
        """

        # pack
        self.leftPane.pack_propagate(False)
        self.rightPane.pack_propagate(False)
        for i, _x in enumerate(self.leftFrames):
            self.leftFrames[i].pack()
            self.rightFrames[i].pack()
            self.leftFrames[i].pack_propagate(False)
            self.rightFrames[i].pack_propagate(False)
            self.leftWidgets[i].add_css(self.bodyCss)
            self.rightWidgets[i].add_css(self.bodyCss)
            self.leftWidgets[i].pack()
            self.rightWidgets[i].pack()

        # meta
        self.numberOfWidgets: int = len(self.leftWidgets)

    def addWidget(self, widget: Widget) -> None:
        # pane selection
        paneDict: dict = {
            "left": self.leftWidgets,
            "right": self.rightWidgets}
        widgetFrame: tkw.HtmlLabel = paneDict[widget.pane][widget.slotNumber]

        # placeholder
        widget.update()
        html: str = widget.render() # widgetSize parameter?
        widgetFrame.load_html(html)
        widgetFrame.add_css(self.bodyCss)

    def refresh(self) -> None:
        logging.info("refreshing screen")
        self.root.update()


if __name__ == "__main__":
    w = Window()
    print(f"There is space for {w.numberOfWidgets} widgets on each side panel")
    
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


    wc = WidgetClock("w1", "* * * * *", 1, "left", 0, configClock)
    wb = WidgetBins("w2", "* * * * *", 1, "left", 1, configBins)
    wr = WidgetRss("w3", "* * * * *", 1, "left", 2, configRss)
    # wb.update()
    wr.update()

    while True:
        wc.update()
        

        w.addWidget(wc)
        w.addWidget(wr)
        w.addWidget(wc)
        w.addWidget(wc)
        w.addWidget(wc)
        w.addWidget(wc)
        w.addWidget(wc)
        w.addWidget(wc)

        w.refresh()