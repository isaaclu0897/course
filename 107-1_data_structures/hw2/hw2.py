#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 23:21:46 2018

@author: wei
"""

def PA_r(height):
    # use Recursively by relation
    def inner_func(n, k):
        if k == 0 or k == n:
            return 1
        else:
            left = inner_func(n-1, k)
            right = inner_func(n-1, k-1)
            return left + right
        
    a = []
    for n in range(height+1):
        b = []
        for k in range(n+1):
            b.append(inner_func(n, k))
        a.append(b)
        
    return a


def PA_n(height):
    # just do it, non-recursion
    a = []
    for n in range(height+1):
        b = []
        for k in range(n+1):
            if k == 0 or k == n:
                b.append(1)
            else:
                b.append(a[n-1][k]+a[n-1][k-1])
        a.append(b)
        
    return a
            

    
def PA_d(height):
    # use combination by formula, but the factorial use recursion
    def inner_func(n, k):
        return int(factorial(n) / ((factorial(k) * factorial(n-k))))
        
    a = []
    for n in range(height+1):
        b = []
        for k in range(n+1):
            b.append(inner_func(n, k))
        a.append(b)
        
    return a

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n-1)

if __name__=="__main__":
    from timeit import repeat as time
    
    print(PA_r(6))
    print(PA_n(6))
    print(PA_d(6))
    
    PA_r_time = time('PA_r(6)', 'from __main__ import PA_r', repeat=1, number=1)
    PA_n_time = time('PA_n(6)', 'from __main__ import PA_n', repeat=1, number=1)
    PA_d_time = time('PA_d(6)', 'from __main__ import PA_d', repeat=1, number=1)
    
    print('recursion          time is {:.4e}'.format(sum(PA_r_time)/len(PA_r_time)))
    print('non-recursion      time is {:.4e}'.format(sum(PA_n_time)/len(PA_n_time)))
    print('direct computation time is {:.4e}'.format(sum(PA_d_time)/len(PA_d_time)))
            
    

