#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:21:14 2018

@author: wei
"""

class Fraction(object):
    def __init__(self, fraction):
        """ object of Fraction
    
        you can input the string into Fraction to create the object of fraction,
        such as input ' 3 / 4 ' into Fraction, this class will automatic remove
        space, you also can operate the method from this class, like get the
        numerator and denominator, it will return you how much is it.
        """
        fraction = "".join(fraction.split(" "))
        self.fraction = fraction
        self._num, self._den = (self.fraction).split('/')
        
    def get_numerator(self):
        return "numerator is {}".format(self._num)
    
    def get_denominator(self):
        return "denominator is {}".format(self._den)
    
    def __repr__(self):
        return "fraction({}, {})".format(self._num, self._den)

if __name__=="__main__":
    h = (Fraction.__init__).__doc__
    print('第三題')
    print(h)
    frac = Fraction('  3 /  4  ')
    num = frac.get_numerator()
    den = frac.get_denominator()
    print(frac, '\n', num, '\n', den)
    print('\n')

    