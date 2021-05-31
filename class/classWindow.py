import screeninfo
import tkinter as tk


class Window():
    def __init__(self, widgetSize=200):
        self.monitors = screeninfo.get_monitors()
        m = self.monitors[0]
        

        # root page
        self.root = tk.Tk()
        self.root.geometry(f"{m.width}x{m.height}+{m.x}+{m.y}")
        # 1440x900+0+0

        # add left and right pane
        self.leftPane = tk.Frame(self.root, background="#000000", width=widgetSize, height=m.height)
        self.rightPane = tk.Frame(self.root, background="#000000", width=widgetSize, height=m.height)
        self.centrePane = tk.Frame(self.root, background="#000000", width=m.width-(2*widgetSize))
        self.leftPane.pack(side="left", fill="x")
        self.rightPane.pack(side="right", fill="x")
        self.centrePane.pack(side="top", fill="both", expand=True)

        # add top pane
        self.topPane = tk.Frame(self.centrePane, background="#000000", height=widgetSize)#, width=m.width-(2*widgetSize), height=widgetSize)
        self.mainPane = tk.Frame(self.centrePane, background="#ffffff", height=m.height-widgetSize)#, width=m.width-(2*widgetSize), height=m.height-widgetSize)
        self.topPane.pack(side="top", fill="x")
        self.mainPane.pack(side="top", fill="x")

        # split panes into widget slots

    def addWidget(self, widget, paneName, slotNumber):
        # pane selection
        paneDict = {
            "left": self.leftPane,
            "top": self.topPane,
            "right": self.rightPane}
        pane = paneDict[paneName]
        # widgetSlot = pane.

        # placeholder
        label = tk.Label(pane, text=widget, fg="white", bg="#000000")
        label.grid(sticky="nw")
        pane.grid_propagate(0)

        # widget.render(pane)




if __name__ == "__main__":
    w = Window()
    w.addWidget("abc", "right")
    w.root.mainloop()