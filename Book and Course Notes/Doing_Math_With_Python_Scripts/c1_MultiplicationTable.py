# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:26:14 2015

@author: SZahn
"""


def multiplicationTable(x):
    ''' Prints the multiplication table for the supplied integer. '''
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(int(x), i, int(x)*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
    multiplicationTable(float(a))
