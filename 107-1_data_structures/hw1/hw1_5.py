#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 00:27:41 2018

@author: wei
"""

def square_root(num, x0=None, count=0):
    """ square_root function
    
    this function can calculate square root,
    you can input square of the number that you what to know,
    the function will use tail recursion until you get the square root. 
    """
    if x0 == None:
        return square_root(num, num/2)
    if count == 20: # here can change your condition of suspend
        return x0
    x0 = (x0 * x0 + num) / (2 * x0) # Newton's formula
    count += 1
    return square_root(num, x0, count)

if __name__=="__main__":
    h = square_root.__doc__
    print('第五題')
    print(h)
    rst = square_root(4563)
    print("the square root is {}\n".format(rst))
    print('\n')
