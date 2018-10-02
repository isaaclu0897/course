#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:16:32 2018

@author: wei
"""

""" 利用 C/C++/Java/Python解出線性方程組
目標：解出三組四元一次方程組
    利用程式語言解出線性方程組，
    解法須從零開始，直至解出 reduced echelon form，
    或為 general solutions。

以下列矩陣作為測試資料:
    S = [[2, -1, 3], 
         [1, 1, 3]]
    
    T = [[1, 2, 3],
         [2, 4, 5]]
    
    U = [[1, -4, 1],
         [2, -1, -3],
         [-1, -3, 4]]
    
    V = [[1, 1, 1, 4],
         [-1, -1, 1, -2],
         [2, -1, 2, 2]]

    W = [[0, 1, -4, 8],
         [2, -3, 2, 1],
         [5, -8, 7, 1]]

    Z = [[0, 3, -6, 6, 4],
         [3, -7, 8, -5, 8],
         [-3, -9, 12, -9, 6]]
"""

import numpy as np
from numpy import matrix


def data(num):
    S = [[2, -1, 3], 
         [1, 1, 3]]

    T = [[1, 2, 3],
         [2, 4, 5]]
    
    U = [[1, -4, 1],
         [2, -1, -3],
         [-1, -3, 4]]
    
    V = [[1, 1, 1, 4],
         [-1, -1, 1, -2],
         [2, -1, 2, 2]]
    
    W = [[0, 1, -4, 8],
         [2, -3, 2, 1],
         [5, -8, 7, 1]]
    
    Z = [[0, 3, -6, 6, 4],
         [3, -7, 8, -5, 8],
         [-3, -9, 12, -9, 6]]
    if num == 1:
        return S
    if num == 2:
        return T
    if num == 3:
        return U
    if num == 4:
        return V
    if num == 5:
        return W
    if num == 6:
        return Z

def scaling():
    pass
def interchange():
    pass
def replacement():
    pass

def inner_change(obj_name, first, second):
        obj_name[first], obj_name[second] = obj_name[second], obj_name[first]


def selection_sort(to_sort, key=None):
    if key != None:
        to_sort = to_sort.tolist()
        compare_list = list(map(key, to_sort))
    else:
        from copy import copy as cp
        compare_list = cp(to_sort)

    i = 0
    while i < len(compare_list):
        lowest = i
        compare_item = compare_list[lowest]
        j = i + 1
        
        while j < len(compare_list):
            if compare_item > compare_list[j] or compare_item == 0:
                lowest = j
                compare_item = compare_list[j]
            j += 1
        
        if lowest != i:
            inner_change(to_sort, lowest, i)
            inner_change(compare_list, lowest, i)

        i += 1
    if key != None:
        return matrix(to_sort)
    return to_sort


    
    

a = matrix(data(1)).astype(np.float64); print(a)

# forward-phase
col = 0
row = 0
pivot = []
row_max, col_max = a.shape
while row < row_max and col < col_max:
    a[row:, col:] = selection_sort(a[row:, col:], key=lambda x: abs(x[0])); print(a)
    
    # let value under pivot be 0 
    i = row + 1
    while i < row_max:
        leading_entry = a.item(i, col)
        if  leading_entry != 0:
            scale = -(a[i, col] / a[row, col])
            a[i] = a[i] + a[row] * scale
            print(a)
        i += 1

    # find pivot(here have some error, must be fix)
    j = col
    while 1:
        if a.item(row, j) != 0:
            pivot.append((row, j))
            break
        if a.item(row, j) == 0:
            j = col + 1
        if j >= col_max:
            print('最後一向free')
            break  
    
    col += 1
    row += 1

# scaling
for i, j in pivot:
#    print(i, j)
    scale = a.item(i, j)
    if scale == 0:
        continue
    a[i] = a[i] / scale
    print(a)

# back-phase
pivot.reverse()
for row, col in pivot:
    i = row
    while i > 0:
        i -= 1
        scale = -(a[i, col] / a[row, col])
        a[i] = a[i] + a[row] * scale
        print(a)
#
#X = {}
#for i in range(a.shape[1]-1):
#    print(i, i)
#    if a.item(i, i) != 1:
#        print('this is inconsistient')
#        
#    X[i+1] = a.item(i, -1)
#print(X)
    
        
        

