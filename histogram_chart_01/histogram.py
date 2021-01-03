
# -*- coding: utf-8 -*-
import pandas as pd

# %% Data

__data = [
1,33,44,63,11,
201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,
401,402,403,404,405,406,447,448,449,440,441,442,
600,660,634,690,
800,900,878  
]

s_data = pd.Series(__data, name="Rating")

# %% Drowing Histogram Chart

s_data.plot.hist(bins=5, title="Rating")