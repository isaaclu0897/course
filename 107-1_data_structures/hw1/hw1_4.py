#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:55:58 2018

@author: wei
"""

def inner_change(obj_name, first, second):
        obj_name[first], obj_name[second] = obj_name[second], obj_name[first]

def selection_sort(to_sort, key=None):
    """ selection function
    
    this is the algorithm of selection sort, you can input a list,
    every Iterator, it will select the minimum value swap the first
    value of list. you also can use it at array of 2-dimension.
    
    such as: 
        selection_sort([[8, 2], [1, 1], [3, 9], [4, 5]], key=lambda x: x[1])
        it will return you [[1, 1], [8, 2], [4, 5], [3, 9]]
    """
    # add one pass to sort another element 
    if key != None:
        compare_list = list(map(key, to_sort))
    else:
        from copy import copy as cp
        compare_list = cp(to_sort)
    
    i = 0
    condition = len(compare_list)
    while i < condition:
        lowest = i # create the lowest pointer
        compare_item = compare_list[lowest]
        j = i + 1 # because i already sort, so j from i+1 to start
        
        while j < condition:
            if compare_item > compare_list[j]:
                lowest = j
                compare_item = compare_list[j]
            j += 1
        
        if lowest != i:
            inner_change(to_sort, lowest, i)
            inner_change(compare_list, lowest, i)

        i += 1
        
    return to_sort

if __name__=="__main__":
    h = selection_sort.__doc__
    print('第四題')
    print(h)
    a_list = [4, 2, 3, 5, 62, 426, 43]
    rst = selection_sort(a_list)
    print(a_list, "-->", rst)
    print('\n')