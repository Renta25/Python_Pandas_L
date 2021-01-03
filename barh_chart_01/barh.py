
# -*- coding: utf-8 -*-
import pandas as pd


# %% Data

__data = {
        "North America" : 1500,
        "South America" : 500,
        "Europe" : 1500,
        "Asia" : 2000,
        "Australia and Oceania" : 1000,
        "Africa": 500,
        "Antartica" : 1
}
s_data = pd.Series(__data, name="Sell")

# %% Draw horizontal bar

plot = s_data.plot.barh(x="Sell")
