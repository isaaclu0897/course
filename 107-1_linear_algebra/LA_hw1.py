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


from numpy import matrix 


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


V = [[1, 1, 1, 4],
     [-1, -1, 1, -2],
     [2, -1, 2, 2]]

Z = [[0, 3, -6, 6, 4],
     [3, -7, 8, -5, 8],
     [-3, -9, 12, -9, 6]]

a = matrix(Z)

col = 0
pointer = (0, 0)
while col < a.shape[1]:
    row = col + 1
    
    if row >= a.shape[0]:
        break
    a[row-1:, col:] = selection_sort(a[row-1:, col:], key=lambda x: abs(x[0]))
    print(a)
    head = row - 1
    while row < a.shape[0]:
        
        k = a.item(row, col)
        print(row, col, k, head)
        
        if  k != 0:
            print(-a[row, 0] , a[head, col])
            scale = -(a[row, col] / a[head, col])
            a[row, :] = a[row, :] + a[head, :] * scale
        row += 1
    print(a, '\n')
    col += 1    
    
