# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:26:14 2015

@author: SZahn
"""


def multiplicationTable(x, y):
    ''' Prints the multiplication table for the supplied integer. '''
    for i in range(1, y+1):
        if x.is_integer() is True:
            print('{0} x {1} = {2}'.format(int(x), i, int(x)*i))
        else:
            print('{0} x {1} = {2}'.format(float(x), i, float(x)*i))


if __name__ == '__main__':
    while True:
        a = float(input('Enter a number: '))
        b = float(input('How many multiples would you like to see: '))
        if b.is_integer() is True:
            multiplicationTable(a, int(b))
            break
        else:
            print('Please enter an integer number of multiples.')
