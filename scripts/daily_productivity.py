from datetime import datetime as dt
from collections import OrderedDict
from datetime import date
import calendar

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_3_2018 = pd.DataFrame.from_csv("productivity_month/3_2018/RescueTime_Report_Productivity__by_day__Mon_Fri_6am_8pm__2018-03-01.csv")
df_4_2018 = pd.DataFrame.from_csv("productivity_month/4_2018/RescueTime_Report_Productivity__by_day__Mon_Fri_6am_8pm__2018-04-01.csv")

df = pd.concat([df_3_2018, df_4_2018], axis=0, join="inner")

productive_days = df.loc[df["Productivity"] == 1]["Time Spent (seconds)"]  + df.loc[df["Productivity"] == 2]["Time Spent (seconds)"]

new_date = productive_days.index.to_datetime()

md = []
weekdays = []
productivity = []
for index, value in enumerate(new_date):
    weekdays.append(calendar.day_name[value.weekday()])
    md.append("{:%m-%d}".format(value, "%Y-%m-%d"))
    productivity.append(productive_days.iloc[index]/60)

weekday_dict = {"Monday": "b", "Tuesday": "r", "Wednesday" : "y", "Thursday" : "g", "Friday" : "k"}

fig = plt.figure()
ax = fig.add_subplot(111)
for index, value in enumerate(md):
    plt.bar(index, productivity[index], color=weekday_dict[weekdays[index]], label=weekdays[index])
#plt.bar(md, productive_days/60)
plt.xticks(rotation=45)
ax.set_ylabel("Minutes")
ax.set_xlabel("Day")
plt.title("Minutes spent on productive tasks")


handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc=4)

plt.savefig("images/MFproductivity.png")
plt.close()

