#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on Sun Oct 28 23:51:40 2018 

@author: wei
"""

class Stack:
    def __init__(self):
        self.item = []
    
    def push(self, item):
        self.item = self.item + item
    
    def pop(self):
        return self.item.pop()

    def isEmtpy(self):
        return self.item == False

    def size(self):
        return len(self.item)
    
    def show(self):
        print(self.item)

def main(n):
    left = ['0']
    right = ['1']
    for i in range(n):
        new = left + right
        stack = Stack()
        stack.push(new)
        left = []
        right = []
        for i in new:
            left.append('0' + i)
            right.append('1' + stack.pop())

    return new




if __name__ == '__main__':
    rst = main(3)
    print(rst)
