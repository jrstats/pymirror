import logging

from classes import Orchestrator, Settings, Window
from classes import WidgetClock, WidgetBins, WidgetRss

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    wc = WidgetClock(
        widgetName="clock", 
        cronSyntax="* * * * * * *", 
        priority=1, 
        config=Settings.CLOCK,
        pane="left",
        slotNumber=0)
    wr = WidgetRss(
        widgetName="rssFeed", 
        cronSyntax="0 * * * * * *", 
        priority=1, 
        config=Settings.RSS,
        pane="right",
        slotNumber=0)
    # wb = WidgetBins(
    #     widgetName="bins",
    #     cronSyntax="0 0 * * * * *",
    #     priority=1,
    #     config=Settings.BINS,
    #     pane="right",
    #     slotNumber=1
    # )
    window = Window()

    o = Orchestrator([wc, wr], window)
    o.live()