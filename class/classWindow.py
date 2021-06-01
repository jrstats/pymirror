import math
import screeninfo
import tkinter as tk
import tkinterweb as tkw


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
        
        # # split panes into widget slots
        self.leftFrames = [tk.Frame(self.leftPane, width=self.widgetSize, height=self.widgetSize + 2*self.paddingY, bg="black") for i in range(widgetsTall)]
        self.rightFrames = [tk.Frame(self.rightPane, width=self.widgetSize, height=self.widgetSize + 2*self.paddingY, bg="black") for i in range(widgetsTall)]
        self.leftWidgets = [tkw.HtmlLabel(i, "<p>Empty widget</p>") for i in self.leftFrames]
        self.rightWidgets = [tkw.HtmlLabel(i, "<p>Empty widget</p>") for i in self.rightFrames]
        

        # pack
        self.leftPane.pack_propagate(0)
        self.rightPane.pack_propagate(0)
        for i, _x in enumerate(self.leftFrames):
            self.leftFrames[i].pack()
            self.rightFrames[i].pack()
            self.leftFrames[i].pack_propagate(0)
            self.rightFrames[i].pack_propagate(0)
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
        # html = widget.render() # widgetSize parameter?
        html = f"<h1>{widget}!</h1>"
        widgetFrame.load_html(html)





if __name__ == "__main__":
    w = Window()
    w.addWidget("abc", "right", 0)
    w.addWidget("def", "right", 1)
    w.addWidget("james", "right", 2)
    w.addWidget("eurovision", "left", 0)
    w.addWidget("floorball", "left", 3)
    w.root.mainloop()