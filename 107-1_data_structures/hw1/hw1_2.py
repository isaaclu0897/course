#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:57:02 2018

@author: wei
"""

import numpy as np

def IDvalidation(IDnumber):
    """ ID of Taiwan checker
    
    you can input your ID number using the type of string,
    that will check it valid or not,
    and return you what problem do your input have.
    
    note:this function is case insensitive,
    so you can input like 'a130637749' or 'A130637749' 
    """
    # define the prefix for city
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
    
    # parser the ID number
    prefix = IDnumber[0].upper()
    sex = int(IDnumber[1])
    midnums = IDnumber[1:9]
    checknum = IDnumber[-1]
    
    if len(IDnumber) != 10:
        return "身份證為總共10碼"
    
    if prefix not in head:
        return "所處縣市不在"
    
    if sex != 1 and sex!= 2:
        return "這是第三性"
    
    # fine the Confirm code
    midnums = head[prefix]['num'] + midnums    
    midnums = np.array([int(i) for i in midnums])
    coefi = np.array([1, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    verify = 10 - sum(midnums * coefi) % 10 # the formula of check
    
    if verify != int(checknum):
        return "失效"
    
    return "有效"
 
if __name__=="__main__":
    rst = IDvalidation('a130637749')
    print("this ID is {}".format(rst))