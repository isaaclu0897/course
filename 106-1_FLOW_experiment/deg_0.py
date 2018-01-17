# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:00:42 2017

@author: wei
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tabulate

os.chdir(r'C:\Users\wei\Desktop\good')
path = r'.\n'
filename = r'ntest_deg20_init65_1.csv'

try:
    for i in range(5):
        filename = filename.split('_')
        filename[-1] = '{}.csv'.format(i+1)
        filename = '_'.join(filename)
        print(filename)
        file = os.path.join(path, filename)
        
        wind_df = pd.read_csv(file)
        wind = np.array(wind_df.ix[:, 0])
        lift = np.array(wind_df.ix[:, 1])
        drop = np.array(wind_df.ix[:, 2])
        headers = ["item", "qty"]
#        print(tabulate.tabulate(wind_df, headers,tablefmt="grid"))
        x_axis = 'speed'
        y_axis = 'force'
        axis = {"speed": "speed, m/s", "force": "force, N"}
        line_label = {'lift' : 'data{}_lift'.format(i+1),
                      'drop' : 'data{}_drop'.format(i+1)}
        
        plt.figure(num=1, figsize=(10, 8))
        plt.xlabel(axis[x_axis])
        plt.ylabel(axis[y_axis])
        plt.title('deg_20_init65_result')
        plt.grid()
        plt.plot(wind, lift, label=line_label['lift'])
        plt.plot(wind, drop, label=line_label['drop'])
        plt.legend(loc='upper left')
except:
    print('123')