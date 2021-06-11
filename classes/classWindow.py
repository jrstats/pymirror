import math
import screeninfo
import tkinter as tk
import tkinterweb as tkw

from typing import List
from .classWidget import Widget
from .classWidgetBins import WidgetBins
from .classWidgetClock import WidgetClock
from .classWidgetRss import WidgetRss
from .classLogger import Logger
from .classSettings import Settings

logger = Logger(__name__, Settings.LOGGER)
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

    def loadWidget(self, widget: Widget) -> None:
        # pane selection
        paneDict: dict = {
            "left": self.leftWidgets,
            "right": self.rightWidgets}
        widgetFrame: tkw.HtmlLabel = paneDict[widget.pane][widget.slotNumber]

        # widget.update()
        # widget.generateHtml()
        logger.info("loading widget")
        widgetFrame.load_html(widget.html, widget.imageBase)
        widgetFrame.add_css(self.bodyCss)

    def refresh(self) -> None:
        logger.info("refreshing screen")
        self.root.update()
