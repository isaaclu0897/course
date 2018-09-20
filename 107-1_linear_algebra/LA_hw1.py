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
        self.obj = obj
    
    @property
    def _num(self):
        if isinstance(self.obj, Iterable):
            if isinstance(self.obj[0], Iterable):
                return (len(self.obj), len(self.obj[0]))
            else:
                return (len(self.obj), )
            
    def __add__(self, other):
        return list(map(lambda x, y: x + y, self.obj, other.obj))
    
    def __mul__(self, scalar):
        return Array([i * scalar for i in self.obj])
    
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
        self.obj = selection_sort(self.obj, key=lambda x: x[col])


    
    def __repr__(self):
        _ = "\n      ".join([str(_) for _ in self.obj])
        return "array({})".format(_)
    
    def __str__(self):
        return "\n".join([str(_) for _ in self.obj])

def inner_change(obj_name, first, second):
        obj_name[first], obj_name[second] = obj_name[second], obj_name[first]


def selection_sort(to_sort, key=None):
    if key != None:
        compare_list = list(map(key, to_sort))

    i = 0
    while i < len(to_sort):
        lowest = i
        compare_item = to_sort[lowest]
        j = i + 1
        
        while j < len(to_sort):
            if compare_item < to_sort[j]:
                lowest = j
                compare_item = to_sort[j]
            j += 1
        
        if lowest != i:
            if key != None:
                inner_change(to_sort, lowest, i)
                inner_change(compare_list, lowest, i)
            else:
                inner_change(to_sort, lowest, i)
        i += 1
        
    return to_sort

if __name__ == "__main__":
    Z = [[0, 3, -6, 6, 4],
         [3, -7, 8, -5, 8],
         [-3, -9, 12, -9, 6]]
    a = Matrix(Z)
    a.interchange(0)
    
    col = 0
    for i in Z:
        tmp = i
        if tmp[col] < i[col]:
            print('do it')
    
#    b = Array([-3, -9, 12, -9, 6])
#    c = Array([-3, -9, 12, -9, 6])
#    b.scaling(-3)

    a
    #print(a.form)
