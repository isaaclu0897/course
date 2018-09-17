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




S = [[2, -1, 3], 
     [1, 1, 3]]

class Array(object):
#    pointer = 0
    
    def __init__(self, obj):
        print(obj)
        self.obj = obj

    def check_leader():
        pass
    
    def interchange():
        pass
    
    def scaling():
        pass
    
    def replacement():
        pass
    
    def __repr__(self):
        _ = "\n      ".join([str(_) for _ in S])
        return "array({})".format(_)
    
    def __str__(self):
        return "\n".join([str(_) for _ in S])
        

#class Matrix(Array):
#    def __init__(self):
#        pass

a = Array(S)
