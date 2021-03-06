from classes import Orchestrator, Settings, Window, Logger
from classes import WidgetClock, WidgetBins, WidgetRss, WidgetWeather, WidgetFootball, WidgetRocketLeague

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
    wf = WidgetFootball(
        widgetName="football",
        cronSyntax="0 * * * * * *",
        priority=1,
        config=Settings.FOOTBALL,
        pane="left",
        slotNumber=1
    )
    wrl = WidgetRocketLeague(
        widgetName="rocketLeague",
        cronSyntax="0 * * * * * *",
        priority=1,
        config=Settings.ROCKET_LEAGUE,
        pane="right",
        slotNumber=2
    )
    window = Window()

    o = Orchestrator([wc, wr, ww, wf, wrl], window, Settings.ORCHESTRATOR)
    o.live()
