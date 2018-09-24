#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:51:08 2018

@author: wei
"""

def bigger(*num):
    max_num = num[0]
    i = 0
    condition = len(num)-1
    while i < condition:
        i += 1
        if num[i] > max_num:
            max_num= num[i]
        else:
            continue

    return max_num

bigger(1, 2, 3, 7, 4, 1, 5)

#%%
import numpy as np

def IDvalidation(IDnumber):
    head = { 'A': {'num': '10', 'city': '台北市'},
             'B': {'num': '11', 'city': '台中市'},
             'C': {'num': '12', 'city': '基隆市'},
             'D': {'num': '13', 'city': '台南市'},
             'E': {'num': '14', 'city': '高雄市'},
             'F': {'num': '15', 'city': '台北縣'},
             'G': {'num': '16', 'city': '宜蘭縣'},
             'H': {'num': '17', 'city': '桃園縣'},
             'I': {'num': '34', 'city': '嘉義市'},
             'J': {'num': '18', 'city': '新竹縣'},
             'K': {'num': '19', 'city': '苗栗縣'},
             'L': {'num': '20', 'city': '台中縣'},
             'M': {'num': '21', 'city': '南投縣'},
             'N': {'num': '22', 'city': '彰化縣'},
             'O': {'num': '35', 'city': '新竹市'},
             'P': {'num': '23', 'city': '雲林縣'},
             'Q': {'num': '24', 'city': '嘉義縣'},
             'R': {'num': '25', 'city': '台南縣'},
             'S': {'num': '26', 'city': '高雄縣'},
             'T': {'num': '27', 'city': '屏東縣'},
             'U': {'num': '28', 'city': '花蓮縣'},
             'V': {'num': '29', 'city': '台東縣'},
             'W': {'num': '32', 'city': '金門縣'},
             'X': {'num': '30', 'city': '澎湖縣'},
             'Y': {'num': '31', 'city': '陽明山'},
             'Z': {'num': '33', 'city': '連江縣'}}
    prefix, midnums, checknum, sex = IDnumber[0].upper(), IDnumber[1:9], IDnumber[-1], int(IDnumber[1])

    if len(IDnumber) != 10:
        return "身份證為總共10碼"
    if prefix not in head:
        return "所處縣市不在"
    if sex != 1 and sex!= 2:
        return "這是第三性"
        
    midnums = head[prefix]['num'] + midnums    
    midnums = np.array([int(i) for i in midnums])
    coefi = np.array([1, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    verify = 10 - sum(midnums * coefi) % 10
    if verify != int(checknum):
        return "驗證失敗"
    return "驗證成功"    

IDvalidation('a130637749')

#%%

class Fraction(object):
    def __init__(self, fraction):
        fraction = "".join(fraction.split(" "))
        self.fraction = fraction
        self._num, self._den = (self.fraction).split('/')
        
    def get_numerator(self):
        return "numerator is {}".format(self._num)
    
    def get_denominator(self):
        return "denominator is {}".format(self._den)
    
    def __repr__(self):
        return "fraction({}, {})".format(self._num, self._den)
a = Fraction('  3 /  4  ')

#%%
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
            if compare_item > compare_list[j]:
                lowest = j
                compare_item = compare_list[j]
            j += 1
        
        if lowest != i:
            inner_change(to_sort, lowest, i)
            inner_change(compare_list, lowest, i)

        i += 1
        
    return to_sort
A = [4, 2, 3, 5, 62, 426, 43]
selection_sort(A)

#%%

def square(num):
    x0 = num / 2
    
    def innerfunc(num, x0):
        if abs(num - x0 * x0) < 0.00001:
            return x0
        x0 = (x0 * x0 + num) / (2 * x0)
        return innerfunc(num, x0)
    
    return innerfunc(num, x0)
square(9)
        
    
    


    
    

