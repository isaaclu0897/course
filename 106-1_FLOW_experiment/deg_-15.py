# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 17:27:09 2017

@author: wei
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\wei\Desktop\good')
path = r'.\n'
filename = r'ndeg_-15_1.csv'
wind_sum = np.array(0)
lift_sum = np.array(0)
drop_sum = np.array(0)
for i in range(3):
    filename = filename.split('_')
    filename[-1] = '{}.csv'.format(i+1)
    filename = '_'.join(filename)
    print(filename)
    file = os.path.join(path, filename)
    
    wind_df = pd.read_csv(file)

    wind = np.array(wind_df.ix[:, 0])
    lift = np.array(wind_df.ix[:, 1])
    drop = np.array(wind_df.ix[:, 2])
    
    plt.plot(wind, lift, wind, drop)