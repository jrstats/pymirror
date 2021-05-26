# 

# %%
import selenium.webdriver
import pandas as pd

driver = selenium.webdriver.Chrome()
postCode = "W5 2AR"
# %%
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
print(df.explode("Due dates"))
# %%
