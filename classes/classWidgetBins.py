import datetime
import logging
import numpy as np
import pandas as pd
import tkinter as tk

from selenium import webdriver
from typing import List, Dict, Any
from .classWidget import Widget


class WidgetBins(Widget):
    def __init__(self, widgetName: str, cronSyntax: str, priority: int, pane: str, slotNumber: int, config: Dict[str, Any]) -> None:
        super().__init__(widgetName, cronSyntax, priority, pane, slotNumber, config)

        # initialise class
        self.output: pd.DataFrame = None


    def update(self) -> None:
        # update output data
        chrome_options: webdriver.ChromeOptions = webdriver.ChromeOptions()
        chrome_options.headless = True
        self.driver: webdriver.Chrome = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.config["baseUrl"])
        self.driver.find_element_by_id("txtLookupPostCode").send_keys(self.config["postCode"])
        self.driver.find_element_by_id("btnAddressLookup").click()

        # select a different address??
        self.driver.find_element_by_name("waste_collection_getData").submit()


        table = self.driver.find_element_by_id("RetrieveAllDataGrid")
        rows = table.find_elements_by_tag_name("tr")

        data: List[List[str]] = [[x.text for x in y.find_elements_by_tag_name("td")] for y in rows]
        self.driver.quit()

        df: pd.DataFrame = pd.DataFrame(data)
        df.columns = df.iloc[0]
        df = df[1:]
        df["Due dates"] = df["Due dates"].str.split("\n")

        df_tall: pd.DataFrame = df.explode("Due dates", ignore_index=True)
        df_tall = df_tall.rename({"Container type": "bin"}, axis=1)
        df_tall = df_tall.loc[lambda df: df["bin"].isin(self.config["binsOfInterest"])]
        df_tall["dateNext"] = pd.to_datetime(df_tall["Due dates"], format="%d/%m/%y")
        df_tall["frequencyDays"] = np.select(
            condlist=[
                df_tall["Frequency"] == "ONCE WEEKLY",
                df_tall["Frequency"] == "FORTNIGHTLY"
            ], 
            choicelist=[
                pd.DateOffset(days=7),
                pd.DateOffset(days=14)
            ])
        df_tall["dateAfter"] = df_tall["dateNext"] + df_tall["frequencyDays"]
        df_tall["daysNext"] = (df_tall["dateNext"] - pd.to_datetime(datetime.date.today())).dt.days
        df_tall["daysNext"] = df_tall["daysNext"].astype(str) + " days"
        df_tall["daysNext"] = df_tall["daysNext"].replace({"0 days": "This morning", "1 days": "Tomorrow morning"})
        df_tall["bin"] = df_tall["bin"].str.replace(" WHEELIE BIN", "")
        df_tall = df_tall.reset_index(drop=True)
        df_tall = df_tall[["bin", "dateNext", "daysNext", "dateAfter"]]
        
        df_summary: pd.DataFrame = df_tall.groupby("bin").first().reset_index()
        df_summary = df_summary.sort_values(["dateNext", "bin"])
        df_summary = df_summary.drop(["dateNext"], axis=1)
        df_summary = df_summary.rename({
            "daysNext": "Next Collection",
            "dateAfter": "Collection Afterwards"
        }, axis=1)

        bin_colour = df_summary.loc[lambda df: df["bin"] != "FOOD BOX"].iloc[0]["bin"].split(" ")[0]

        self.output = (df_summary, bin_colour)
        logging.info(f"updated widget {self.widgetName} at: {datetime.datetime.now()}")

    def generateHtml(self) -> None:
        # get dataframe
        html: str = self.output[0].to_html(index=False)
        html = html.replace("<th></th>", "")

        # # get colour box
        # if self.output[1].lower() == "blue":
        #     html += """\n<div style="height:10 width:100 color:blue;"></div>"""
        # elif self.output[1].lower() == "black":
        #     html += """<p>&#9633;</p>"""

        self.html: str = html


