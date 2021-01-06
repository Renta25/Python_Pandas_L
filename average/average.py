#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

# %% data
age_list = [ 19, 20, 21, 20, 21, 19, 21, 19]

age_sera = pd.Series(age_list, name="age")

# %% Average

average = age_sera.mean()

