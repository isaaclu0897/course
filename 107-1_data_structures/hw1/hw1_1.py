#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:30:07 2018

@author: wei
"""

def bigger(first_num, *num):
    """ Compare size of numbers
    
    this's function, need you to input more than two same type data.
    just like 2 numbers, 2 lists, or 2 tuple.
    but can not input the string, it will not work.
    """
    
    max_num = first_num
    i = 0
    condition = len(num)-1
    while i < condition:
        i += 1
        if num[i] > max_num:
            max_num= num[i]
        else:
            continue

    return max_num

if __name__=="__main__":
    h = bigger.__doc__
    print('第一題')
    print(h)
    rst= bigger(1, 2, 3, 7, 4, 1, 5)
    print("the one of result is {}".format(rst))
    print('\n')
