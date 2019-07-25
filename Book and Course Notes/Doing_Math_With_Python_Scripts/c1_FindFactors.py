# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:19:25 2015

@author: SZahn
"""


def isFactor(a, b):
    ''' Returns whether or not number a is a factor of number b.'''
    if b % a == 0:
        return True
    else:
        return False


def findFactors(x):
    ''' Returns all factors of the supplied number. '''
    for i in range(1, x+1):
        if x % i == 0:
            print(i)


if __name__ == '__main__':
    x = float(input('Please type a number: '))
    if x > 0 and x.is_integer():
        findFactors(int(x))
    else:
        print('Please enter a positive integer.')
