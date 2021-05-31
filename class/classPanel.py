import screeninfo
import tkinter as tk


class Panel():
    def __init__(self, widgetSize=200):
        self.monitors = screeninfo.get_monitors()
        m = self.monitors[0]
        

        # root page
        self.root = tk.Tk()
        self.root.geometry(f"{m.width}x{m.height}+{m.x}+{m.y}")
        # 1440x900+0+0

        self.leftPane = tk.Frame(self.root, background="#000000", width=widgetSize, height=m.height)
        self.rightPane = tk.Frame(self.root, background="#000000", width=widgetSize, height=m.height)
        self.centrePane = tk.Frame(self.root, background="#000000", width=m.width-(2*widgetSize))

        self.leftPane.pack(side="left", fill="x")
        self.rightPane.pack(side="right", fill="x")
        self.centrePane.pack(side="top", fill="both", expand=True)

        self.topPane = tk.Frame(self.centrePane, background="#000000", height=widgetSize)#, width=m.width-(2*widgetSize), height=widgetSize)
        self.mainPane = tk.Frame(self.centrePane, background="#ffffff", height=m.height-widgetSize)#, width=m.width-(2*widgetSize), height=m.height-widgetSize)
        self.topPane.pack(side="top", fill="x")
        self.mainPane.pack(side="top", fill="x")



if __name__ == "__main__":
    p = Panel()
    p.root.mainloop()