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

#import numpy as np
#from numpy import matrix
#
#class my_matrix(matrix):
#    def __init__(self, data):
#        super(my_matrix, self).__init__(data)


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


    
    

a = matrix(data(2)).astype(np.float64); print(a, '\n')

# forward-phase
col = 0
row = 0
pivot = []
row_max, col_max = a.shape
while row < row_max and col < col_max:
    a[row:, col:] = selection_sort(a[row:, col:], key=lambda x: abs(x[0])); print(a, '\n')
    
    # let value under pivot be 0 
    i = row + 1
    while i < row_max:
        leading_entry = a.item(i, col)
        if  leading_entry != 0:
            scale = -(a[i, col] / a[row, col])
            a[i] = a[i] + a[row] * scale
            print(a, '\n')
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
    print(a, '\n')

# back-phase
pivot.reverse()
for row, col in pivot:
    i = row
    while i > 0:
        i -= 1
        scale = -(a[i, col] / a[row, col])
        a[i] = a[i] + a[row] * scale
        print(a, '\n')

# get the general solution
pivot.reverse()
X = {}
count = 1
for i, j in pivot:
    print(i, j)
        
    X['x{}'.format(count)] = a.item(i, -1)
    count += 1
print(X)
##from scipy.linalg import solve
#b = a[:, -1]
#c = a[:, :-1]
#rst = solve(c, b)
#print(rst)
#x1 = 2 - x2
#x2 = 1
##%%
#from scipy.linalg import solve
#a = [[ 1.          ,0.         ,-1.85714286],
#     [-0.          ,1.         ,-0.71428571],
#     [ 0.          ,0.         , 0.        ]] 
#a = np.matrix(a)
#b = a[:, -1]
#c = a[:, :-1]
#rst = solve(a)
#%%


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
    


import numpy as np
from numpy import matrix

class my_matrix(matrix):
    
    @staticmethod
    def __selection_sort(to_sort, key=lambda x: abs(x[0])):
        def inner_change(obj_name, first, second):
            obj_name[first], obj_name[second] = obj_name[second], obj_name[first]
            
        to_sort = to_sort.tolist()
        compare_list = list(map(key, to_sort))
    
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
        return matrix(to_sort)

    def forward_phase(self):
        row = 0
        col = 0
        self.pivot = []
        row_max, col_max = self.shape
        while row < row_max and col < col_max:
            self[row:, col:] = self.__selection_sort(self[row:, col:]); print(a, '\n')
            
            # let value under pivot be 0 
            i = row + 1
            while i < row_max:
                leading_entry = self.item(i, col)
                if  leading_entry != 0:
                    scale = -(self[i, col] / self[row, col])
                    self[i] = self[i] + self[row] * scale
                    print(self, '\n')
                i += 1
        
            # find pivot(here have some error, must be fix)
            j = col
            while 1:
                if self.item(row, j) != 0:
                    self.pivot.append((row, j))
                    break
                if self.item(row, j) == 0:
                    j = col + 1
                if j >= col_max:
                    print('最後一向free')
                    return  
    
            col += 1
            row += 1
        
        
    
        
        
        
        
a = data(2)
a = my_matrix(a).astype(np.float64)
a.forward_phase()
#a.forward_phase(1)
#, key=lambda x: abs(x[0])

#col = 0
#row = 0
#pivot = []
#row_max, col_max = a.shape
#while row < row_max and col < col_max:
#    a[row:, col:] = selection_sort(a[row:, col:], key=lambda x: abs(x[0])); print(a, '\n')
#    
#    # let value under pivot be 0 
#    i = row + 1
#    while i < row_max:
#        leading_entry = a.item(i, col)
#        if  leading_entry != 0:
#            scale = -(a[i, col] / a[row, col])
#            a[i] = a[i] + a[row] * scale
#            print(a, '\n')
#        i += 1
#
#    # find pivot(here have some error, must be fix)
#    j = col
#    while 1:
#        if a.item(row, j) != 0:
#            pivot.append((row, j))
#            break
#        if a.item(row, j) == 0:
#            j = col + 1
#        if j >= col_max:
#            print('最後一向free')
#            break  
#    
#    col += 1
#    row += 1
















