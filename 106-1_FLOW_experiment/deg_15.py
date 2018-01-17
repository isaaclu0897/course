# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 17:24:36 2017

@author: wei
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tabulate


os.chdir(r'C:\Users\wei\Desktop\good')
path = r'.\n'
filename = r'ndeg_0_3.csv'


print(filename)
file = os.path.join(path, filename)

wind_df = pd.read_csv(file)
wind = np.array(wind_df.ix[:, 0])
lift = np.array(wind_df.ix[:, 1])
drop = np.array(wind_df.ix[:, 2])

wind_n = []
lift_n = []
drop_n = []
for i in range(len(wind)-1):
    if abs(wind[i]-wind[i+1]) >= 0.1:
        insert_wind = (wind[i]+wind[i+1]) / 2
        wind_n.append(wind[i])
        wind_n.append(insert_wind)
        
        insert_lift = (lift[i]+lift[i+1]) / 2
        lift_n.append(lift[i])
        lift_n.append(insert_lift)
        
        insert_drop = (drop[i]+drop[i+1]) / 2
        drop_n.append(drop[i])
        drop_n.append(insert_drop)
    else:
        wind_n.append(wind[i])
        lift_n.append(lift[i])
        drop_n.append(drop[i])
wind_n2 = []
lift_n2 = []
drop_n2 = []
for i in range(len(wind_n)-1):
    if abs(wind_n[i]-wind_n[i+1]) >= 0.1:
        insert_wind = (wind_n[i]+wind_n[i+1]) / 2
        wind_n2.append(wind_n[i])
        wind_n2.append(insert_wind)
        
        insert_lift = (lift_n[i]+lift_n[i+1]) / 2
        lift_n2.append(lift_n[i])
        lift_n2.append(insert_lift)
        
        insert_drop = (drop_n[i]+drop_n[i+1]) / 2
        drop_n2.append(drop_n[i])
        drop_n2.append(insert_drop)
    else:
        wind_n2.append(wind_n[i])
        lift_n2.append(lift_n[i])
        drop_n2.append(drop_n[i])
        
wind_n3 = []
lift_n3 = []
drop_n3 = []
for i in range(len(wind_n2)-1):
    if abs(wind_n2[i]-wind_n2[i+1]) >= 0.1:
        insert_wind = (wind_n2[i]+wind_n2[i+1]) / 2
        wind_n3.append(wind_n2[i])
        wind_n3.append(insert_wind)
        
        insert_lift = (lift_n2[i]+lift_n2[i+1]) / 2
        lift_n3.append(lift_n2[i])
        lift_n3.append(insert_lift)
        
        insert_drop = (drop_n2[i]+drop_n2[i+1]) / 2
        drop_n3.append(drop_n2[i])
        drop_n3.append(insert_drop)
    else:
        wind_n3.append(wind_n2[i])
        lift_n3.append(lift_n2[i])
        drop_n3.append(drop_n2[i])


print(len(wind_n), len(wind_n2))

headers = ["item", "qty"]
#print(tabulate.tabulate(wind_df, headers,tablefmt="grid"))
x_axis = 'speed'
y_axis = 'force'
axis = {"speed": "speed, °C", "force": "force, kJ/kgK"}
line_label = {'lift' : 'data{}_lift'.format(3),
              'drop' : 'data{}_drop'.format(3)}
'''
plt.figure(num=1, figsize=(10, 8))
plt.xlabel(axis[x_axis])
plt.ylabel(axis[y_axis])
plt.title('result')
plt.grid()
plt.plot(wind, lift, label=line_label['lift'])
plt.plot(wind, drop, label=line_label['drop'])
plt.legend(loc='best')

plt.figure(num=2, figsize=(10, 8))
plt.xlabel(axis[x_axis])
plt.ylabel(axis[y_axis])
plt.title('result_1')
plt.grid()
plt.plot(wind_n, lift_n, label=line_label['lift'])
plt.plot(wind_n, drop_n, label=line_label['drop'])
plt.legend(loc='best')

plt.figure(num=3, figsize=(10, 8))
plt.xlabel(axis[x_axis])
plt.ylabel(axis[y_axis])
plt.title('result_2')
plt.grid()
plt.plot(wind_n2, lift_n2, label=line_label['lift'])
plt.plot(wind_n2, drop_n2, label=line_label['drop'])
plt.legend(loc='best')

plt.figure(num=4, figsize=(10, 8))
plt.xlabel(axis[x_axis])
plt.ylabel(axis[y_axis])
plt.title('result_3')
plt.grid()
plt.plot(wind_n3, lift_n3, label=line_label['lift'])
plt.plot(wind_n3, drop_n3, label=line_label['drop'])
plt.legend(loc='best')
'''
'''
plt.figure(num=1, figsize=(10, 8))
plt.xlabel(axis[x_axis])
plt.ylabel(axis[y_axis])
plt.title('result')
plt.grid()
plt.plot(wind, lift, label=line_label['lift'])
plt.plot(wind, drop, label=line_label['drop'])
plt.plot(wind_n, lift_n, label=line_label['lift'])
plt.plot(wind_n, drop_n, label=line_label['drop'])
plt.plot(wind_n2, lift_n2, label=line_label['lift'])
plt.plot(wind_n2, drop_n2, label=line_label['drop'])
plt.plot(wind_n3, lift_n3, label=line_label['lift'])
plt.plot(wind_n3, drop_n3, label=line_label['drop'])
plt.legend(loc='best')
'''