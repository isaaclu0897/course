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
    可以得話解出 general solutions。

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

# set test case
def data(num):
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
    if num == 1:
        return S
    if num == 2:
        return T
    if num == 3:
        return U
    if num == 4:
        return V
    if num == 5:
        return W
    if num == 6:
        return Z
    

import functools
import numpy as np
from numpy import matrix

# try to use wrapper to prettify output
def log_method(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
#        print('\tdo {}():'.format(func.__name__))
        func(*args, **kw)
#        rst_str = np.round(args[0], 4).__str__().replace('\n', '\n\t ')
#        print('\t method_rst: \n', '\t {} \n'.format(rst_str))
    return wrapper

def log_method_phase(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('\n', '___'*18)
        print('\n', 'do {}():'.format(func.__name__))
        rst = func(*args, **kw)
        print('{}_rst: \n'.format(func.__name__), np.round(rst, 4))
        return rst
    return wrapper

class my_matrix(matrix):
    """ my idea
    
    in this class, i will divide it into three step.
    like forward_phase, back_phase, and get_solution of function.
    but no just like that, you need to three elementary row operate,
    such as interchange, scalong and replacement, then i define that method. 
    
    so we just need to divide and conqer, then we can get the final solution,
    
    note: the reduced echelon from actually is result of back_phase.
    """    
    
    @log_method_phase
    def forward_phase(self):
        row = 0
        col = 0
        self._pivot = []
        self.lastrow = False
        row_max, col_max = self.shape
        while row < row_max and col < col_max:
            self.interchange(row, col)
            # let value under pivot be 0 
            i = row + 1
            while i < row_max:
                leading_entry = self.item(i, col)
                if  leading_entry != 0:
                    self.replacement(row, col, i)
                i += 1
        
            # find pivot
            j = col
            while 1:
                if self.item(row, j) != 0:
                    self._pivot.append((row, j))
                    break
                if self.item(row, j) == 0:
                    j = col + 1
                if j >= col_max:
                    print('\t最後一列要再次檢查')
                    self.lastrow = True
                    self.scaling()
                    return self
    
            col += 1
            row += 1
        self.scaling()
        return self
            
    
    @log_method_phase
    def back_phase(self):
        a = self._pivot
        pivot = a
        for row, col in pivot:
            i = row
            while i > 0:
                i -= 1
                self.replacement(row, col, i)
        return np.round(self, 4)
    
                
    @log_method
    def interchange(self, row, col):
        self[row:, col:] = self._selection_sort(self[row:, col:])
    
    @log_method
    def scaling(self):
        for i, j in self._pivot:
            scale = self.item(i, j)
            if scale == 0:
                continue
            self[i] = self[i] / scale
            
    @log_method
    def replacement(self, row, col, i):
        scale = -(self[i, col] / self[row, col])
        self[i] = self[i] + self[row] * scale
        
    @staticmethod
    def _selection_sort(to_sort, key=lambda x: abs(x[0])):
        def inner_change(obj_name, first, second):
            obj_name[first], obj_name[second] = \
            obj_name[second], obj_name[first]
            
        to_sort = to_sort.tolist()
        compare_list = list(map(key, to_sort))
    
        i = 0
        while i < len(compare_list):
            lowest = i
            compare_item = compare_list[lowest]
            j = i + 1
            
            while j < len(compare_list):
                if compare_item > compare_list[j] or compare_item == 0:
                    lowest = j
                    compare_item = compare_list[j]
                j += 1
            
            if lowest != i:
                inner_change(to_sort, lowest, i)
                inner_change(compare_list, lowest, i)
    
            i += 1
        return my_matrix(to_sort)
    
    
    def get_solution(self):
        X = {}
        print('\n\nthis is {} type.'.format(self._type))
        if self._type == 'unit square':
            print('that solution will equal to ordinary vector.')
            for i in range(self.coefficient.shape[0]):
                X['x{}'.format(i+1)] = round(self.item(i, -1), 4)
            print('so, only one solution is: ', X)
        elif self._type == 'many_solution':
            for i, j in self._pivot:
                j += 1
                X['x{}'.format(i+1)] = str(round(self.item(i, -1), 4))
                while j < self.shape[1]-1:
                    obj = round(self.item(i, j), 4)
                    if obj == 0:
                        j+=1
                        continue
                    a = ' + {}x{} '.format(-obj, j+1)
                    X['x{}'.format(i+1)] = X['x{}'.format(i+1)] + a
                    j+=1
            X['x{}'.format(i+2)] = 'free'
            print('so, the general solution is:\n', X)
        else:
            print('No solution in here.')   
            
    def check_lastrow(self):
        if self.lastrow:
            self.lastrow = False
            if np.all(self[-1] == np.matrix(np.zeros(self.shape[0]))):
                return self[:-1, :]
        return self
    
    def matrix_type(self):
        self._type = None
        self.constant = self[:, -1]
        self.coefficient = self[:, :-1]
        if self.coefficient.shape[0] == self.coefficient.shape[1]:
            self._type = 'square'
            if np.all(self.coefficient == \
                      np.asmatrix(np.eye(self.coefficient.shape[0]))):
                self._type = 'unit square'
            else:
                self._type = 'inconsistient'
        else:
            self._type = 'many_solution'
        
        
    

                
        
        
        
if __name__=="__main__":
#    想看操作步驟可以把,log_method(func)裡的三行註解打開,
#    你可以看到所有化簡的過程
    
    print(my_matrix.__doc__)
    for i in range(1, 7):
        a = data(i)
        a = my_matrix(a).astype(np.float64)
        print('test case {}:\n'.format(i), a.__repr__())
        a.forward_phase()
        a.back_phase()
        a = a.check_lastrow()
        a.matrix_type()
        a.get_solution()
        print('\n\n', '==='*20)











