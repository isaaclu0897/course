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

from collections import Iterable



class Array(object):
#    pointer = 0
    
    
    def __init__(self, obj):
        self.obj = obj
        
        self.__idx = 0
    
    @property
    def _num(self):
        if isinstance(self.obj, Iterable):
            if isinstance(self.obj[0], Iterable):
                return (len(self.obj), len(self.obj[0]))
            else:
                return (len(self.obj), )
        
    def __add__(self, other):
        return Array(list(map(lambda x, y: x + y, self.obj, other.obj)))
    
    def __mul__(self, scalar):
        return Array([i * scalar for i in self.obj])
    
    def scaling(self, remove_num):
        self.obj = list(map(lambda x: x / remove_num, self.obj))
    
    def __getitem__(self, index):
        return self.obj[index]
    
    def __setitem__(self, index, value):
        self.obj[index] = value
    
    def __len__(self):
        return len(self.obj)
        
    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.obj[self.__idx]
        except IndexError:
            raise StopIteration()
        self.__idx += 1
        return item
    
    def __repr__(self):
        self.obj = [round(i, 3) for i in self.obj] 
        return "array({})".format(self.obj)
    
    def __str__(self):
        self.obj = [round(i, 3) for i in self.obj] 
        return "{}".format(self.obj)



class Matrix(Array):
    def __init__(self, array):
        super(Matrix, self).__init__(array)
        self.obj = [Array(i) for i in self.obj]
#        self.array = [Array(i) for i in array]
#        self.array = array
#        self.pivot_col_pointer = 0
    
    @property
    def form(self):
        return (self._num)
    
    def check_leader():
    # sort the order of array, if leadering entry
        pass

    def replacement(self, a, b, coefi):
        self.obj[a] = self.obj[b].__mul__(coefi) + self.obj[a]
    
    def interchange(self, col):
        self.obj = selection_sort(self.obj, key=lambda x: x[col])

    

    
    def __repr__(self):
        _ = "\n       ".join([str(_) for _ in self.obj])
        return "matrix({})".format(_)
    
    def __str__(self):
        return "\n".join([str(_) for _ in self.obj])

def inner_change(obj_name, first, second):
        obj_name[first], obj_name[second] = obj_name[second], obj_name[first]


def selection_sort(to_sort, key=None):
    if key != None:
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
            if compare_item < compare_list[j]:
                lowest = j
                compare_item = compare_list[j]
            j += 1
        
        if lowest != i:
            inner_change(to_sort, lowest, i)
            inner_change(compare_list, lowest, i)

        i += 1
        
    return to_sort

if __name__ == '__main__':
    
    Z = [[0, 3, -6, 6, 4],
         [3, -7, 8, -5, 8],
         [-3, -9, 12, -9, 6]]
    
    a = Matrix(Z)
    a.interchange(0)
    for col in [0]:
        for idx in range(1, a.form[0]):
            print(idx, col)
            if a[idx][col] != 0:
                print("do it{}{}   {}".format(idx, col, a[idx][col]))
            
    
#    b = Array([-3, -9, 12, -9, 6])
#    c = Array([-3, -9, 12, -9, 6])
#    b.scaling(-3)

#    a
    #print(a.form)
#%%
# 写一个n*n非奇异线性方程组求解函数
# Elimination：消元
def Elimination1(A):
    for i in range(1, A.shape[0]):
        A[i] = A[i] - A[0]*(A[i,0]/A[0,0])      
    return(A)

def Elimination(A):
    j = A.shape[0] - 1
    i = 0
    while j > 0:
        A[i:,i:] = Elimination1(A[i:,i:])
        i = i + 1
        j = j - 1
    return(A)

import numpy as np
A = np.matrix([[1,2,3,6],[3,1,0,3],[-1,1,0,3]])
Elimination(A)

#%%

A = [[3, 7, 7, 6],
     [1, 3, 4, -2],
     [0, 1, 4, -5]]

A = [[1, 0, 3, 0, 2],
     [0, 1, 0, -3, 3],
     [0, -2, 3, 2, 1],
     [3, 0, 0, 7, -5]]

A = [[1, 2, 1, 4],
     [0, 1, -1, 1],
     [1, 3, 0, 0]]

A = [[1, 3, 5, 7],
     [3, 5, 7, 9],
     [5, 7, 9, 1]]

A = [[3, -4, 2, 0],
     [-9, 12, -6, 0],
     [-6, 8, -4, 0]]




A = Matrix(A)
