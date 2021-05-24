# %%

import datetime

refresh_rate = 60
date_format = "%Y-%m-%d"
time_format = "%H:%M"

now = datetime.datetime.now()
print(now.strftime(date_format))
print(now.strftime(time_format))
# %%
