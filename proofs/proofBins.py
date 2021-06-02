# %%
import datetime
import numpy as np
import pandas as pd
import selenium.webdriver

postCode = "W5 2AR"
# %%
driver = selenium.webdriver.Chrome()
driver.get("https://www.ealing.gov.uk/site/custom_scripts/waste_collection/waste_collection.aspx")
driver.find_element_by_id("txtLookupPostCode").send_keys(postCode)
driver.find_element_by_id("btnAddressLookup").click()


# %%
# select a different address??


# %%
driver.find_element_by_name("waste_collection_getData").submit()


# %%
table = driver.find_element_by_id("RetrieveAllDataGrid")
rows = table.find_elements_by_tag_name("tr")
row0 = rows[0]

data = [[x.text for x in y.find_elements_by_tag_name("td")] for y in rows]
driver.quit()


# %%


df = pd.DataFrame(data)
df.columns = df.iloc[0]
df = df[1:]
df["Due dates"] = df["Due dates"].str.split("\n")
# %%
binsOfInterest = ["BLUE RECYCLING WHEELIE BIN", "FOOD BOX", "BLACK RUBBISH WHEELIE BIN"]
df_tall = df.explode("Due dates", ignore_index=True)
df_tall = df_tall.rename({"Container type": "bin"}, axis=1)
df_tall = df_tall.loc[lambda df: df["bin"].isin(binsOfInterest)]
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
df_tall = df_tall.reset_index(drop=True)
df_tall = df_tall[["bin", "dateNext", "daysNext", "dateAfter"]]
df_summary = df_tall.groupby("bin").first().reset_index()
df_summary = df_summary.sort_values(["dateNext", "bin"])
df_summary = df_summary.drop(["dateNext"], axis=1)
df_summary = df_summary.rename({
    "daysNext": "Next Collection",
    "dateAfter": "Collection Afterwards"
}, axis=1)
# %%
df_summary.loc[lambda df: df["bin"] != "FOOD BOX"].iloc[0]["bin"].split(" ")[0]

# %%
print(df_summary.to_html(index=False))
# %%
