from classes import Orchestrator, Settings, Window, Logger
from classes import WidgetClock, WidgetBins, WidgetRss, WidgetWeather

if __name__ == "__main__":
    logger = Logger(__name__, Settings.LOGGER)
    logger.info("starting mirror")
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
    ww = WidgetWeather(
        widgetName="weather",
        cronSyntax="0 * * * * * *",
        priority=1,
        config=Settings.WEATHER,
        pane="right",
        slotNumber=1)
    window = Window()

    o = Orchestrator([wc, wr, ww], window, Settings.ORCHESTRATOR)
    o.live()
