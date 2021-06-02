import math
import screeninfo
import tkinter as tk
import tkinterweb as tkw

from classWidgetClock import WidgetClock


class Window():
    def __init__(self, widgetSize=200):
        self.widgetSize = widgetSize
        self.monitors = screeninfo.get_monitors()
        m = self.monitors[0]
        

        # root page
        self.root = tk.Tk()
        self.root.geometry(f"{m.width}x{m.height}+{m.x}+{m.y}")
        # 1440x900+0+0

        # add left and right pane
        self.leftPane = tk.Frame(self.root, background="#000000", width=self.widgetSize, height=m.height)
        self.rightPane = tk.Frame(self.root, background="#000000", width=self.widgetSize, height=m.height)
        self.centrePane = tk.Frame(self.root, background="#ffffff", width=m.width-(2*self.widgetSize))
        self.leftPane.pack(side="left", fill="x")
        self.rightPane.pack(side="right", fill="x")
        self.centrePane.pack(side="top", fill="both", expand=True)

        # calculate number of slots
        widgetsTall = math.floor(m.height/self.widgetSize)
        self.paddingY = (m.width - widgetsTall*self.widgetSize)/(2*(self.widgetSize + 1))
        self.widgetWidth = self.widgetSize
        self.widgetHeight = self.widgetSize + 2*self.paddingY
        
        # split panes into widget slots
        self.leftFrames = [tk.Frame(self.leftPane, width=self.widgetWidth, height=self.widgetHeight, bg="black") for i in range(widgetsTall)]
        self.rightFrames = [tk.Frame(self.rightPane, width=self.widgetWidth, height=self.widgetHeight, bg="black") for i in range(widgetsTall)]
        self.leftWidgets = [tkw.HtmlLabel(i, "<p>Empty widget</p><hr>", width=self.widgetWidth, height=self.widgetHeight) for i in self.leftFrames]
        self.rightWidgets = [tkw.HtmlLabel(i, "<p>Empty widget</p><hr>", width=self.widgetWidth, height=self.widgetHeight) for i in self.rightFrames]
        

        # css template
        self.bodyCss = """
        body {
            background-color: black;
            color: white
        }
        """

        # pack
        self.leftPane.pack_propagate(0)
        self.rightPane.pack_propagate(0)
        for i, _x in enumerate(self.leftFrames):
            self.leftFrames[i].pack()
            self.rightFrames[i].pack()
            self.leftFrames[i].pack_propagate(0)
            self.rightFrames[i].pack_propagate(0)
            self.leftWidgets[i].add_css(self.bodyCss)
            self.rightWidgets[i].add_css(self.bodyCss)
            self.leftWidgets[i].pack()
            self.rightWidgets[i].pack()

        # meta
        self.numberOfWidgets = len(self.leftWidgets)

    def addWidget(self, widget, paneName, slotNumber):
        # pane selection
        paneDict = {
            "left": self.leftWidgets,
            "right": self.rightWidgets}
        widgetFrame = paneDict[paneName][slotNumber]

        # placeholder
        html = widget.render() # widgetSize parameter?
        widgetFrame.load_html(html)
        widgetFrame.add_css(self.bodyCss)

    def refresh(self):
        self.root.update()
        # self.rightWidgets[0].update() # doesn't work




if __name__ == "__main__":
    w = Window()
    print(f"There is space for {w.numberOfWidgets} widgets on each side panel")
    
    config = {
        "dateFormat": "%Y-%m-%d",
        "timeFormat": "%H:%M:%S"
    }
    wc = WidgetClock("w1", "* * * * *", 1, config)
    
    while True:
        wc.update()

        w.addWidget(wc, "right", 0)
        w.addWidget(wc, "right", 1)
        w.addWidget(wc, "right", 2)
        w.addWidget(wc, "right", 3)
        w.addWidget(wc, "left", 0)
        w.addWidget(wc, "left", 1)
        w.addWidget(wc, "left", 2)
        w.addWidget(wc, "left", 3)

        w.refresh()