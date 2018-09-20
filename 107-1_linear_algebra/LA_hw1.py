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

S = [[2, -1, 3], 
     [1, 1, 3]]


class Array(object):
#    pointer = 0
    
    def __init__(self, obj):
#        print(obj)
        self.obj = obj
    
    @property
    def _num(self):
        if isinstance(self.obj, Iterable):
            if isinstance(self.obj[0], Iterable):
                return (len(self.obj), len(self.obj[0]))
            else:
                return (len(self.obj), )
    

    def scaling(self, remove_num):
        self.obj = list(map(lambda x: x / remove_num, self.obj))
    
    def __repr__(self):
        return "array({})".format(self.obj)
    
    def __str__(self):
        return "{}".format(self.obj)



class Matrix(Array):
    def __init__(self, array):
        super(Matrix, self).__init__(array)
#        self.array = array
#        self.pivot_col_pointer = 0
    
    @property
    def form(self):
        return (self._num)
    
    def check_leader():
    # sort the order of array, if leadering entry
        pass

    def replacement():
        pass
    
    def interchange(self, col):
        return (self.obj).sort(key=lambda x:x[col], reverse=True)
#        tmp = self.obj[0]
#        print(tmp)
#        for i in self.obj:
#            if i[col] > tmp[col]:
#                tmp = self.obj
#        return tmp
    
    def __repr__(self):
        _ = "\n      ".join([str(_) for _ in self.obj])
        return "array({})".format(_)
    
    def __str__(self):
        return "\n ".join([str(_) for _ in self.obj])
    

a = Matrix(S)
b = Array([2, 2, 3])
b.scaling(2)
#print(a.form)
#%%
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
        while j < len(to_sort):
            
            if compare_item > compare_list[j]:
                lowest = j
                compare_item = compare_list[j]
            j += 1


        if lowest != i:
            def inner_change(obj_name, first, second):
                obj_name[first], obj_name[second] = obj_name[second], obj_name[first]
            inner_change(to_sort, lowest, i)
            inner_change(compare_list, lowest, i)
        i += 1
        
    return to_sort

    
Z = [[0, 3, -6, 6, 4],
     [3, -7, 8, -5, 8],
     [-3, -9, 12, -9, 6]]
selection_sort([-3, -9, 12, -9, 6])
selection_sort(Z, key=lambda x: x[0])
##%%
#def insertion_sort(to_sort):
#	i=0
#	while i <= len(to_sort)-1:
#		hole = i;
#		compare_item = to_sort[i]
#		while hole > 0 and to_sort[hole-1]  > compare_item:
#			to_sort[hole] = to_sort[hole-1]
#			hole-=1
#		to_sort[hole] = compare_item
#		i+=1
#	return to_sort