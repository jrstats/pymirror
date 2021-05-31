import datetime
import logging
import tkinter as tk
from classWidget import Widget
from classOrchestrator import Orchestrator


class WidgetClock(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, config: dict):
        super().__init__(widgetName, cronSyntax, priority, config)
        self.output = ('', '')

        ## initialise widget pane

    def update(self):
        now = datetime.datetime.now()
        date = now.strftime(self.config["dateFormat"])
        time = now.strftime(self.config["timeFormat"])
        self.output = (time, date)
        
        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def render(self, pane):
        time_label = tk.Label(pane, text=self.output[0], fg="white", bg="#000000")
        date_label = tk.Label(pane, text=self.output[1], fg="white", bg="#000000")
        time_label.grid(row=1,sticky="nw")
        date_label.grid(row=2,sticky="nw")
        
        pane.grid_propagate(0)

if __name__ == "__main__":
    config = {
        "dateFormat": "%Y-%m-%d",
        "timeFormat": "%H:%M:%S"
    }
    wc = WidgetClock("w1", "* * * * *", 1, config)
    root = tk.Tk()
    root.geometry("200x200")
    frame = tk.Frame(root, background="#000000", width=200, height=200)
    frame.pack()

    wc.update()
    wc.render(frame)
    root.mainloop()