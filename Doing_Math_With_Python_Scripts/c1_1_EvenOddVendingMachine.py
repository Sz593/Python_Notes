# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 07:41:41 2015

@author: SZahn
"""


def evenOddVend(x):
    if x % 2 == 0:
        print('{0} is an even number'.format(x))
#        print('The next 9 even integers are:')
        for i in range(x, x+18, 2):
            print(i, end=', ')
        print(x+18)
    elif x % 2 == 1:
        print('{0} is an odd number'.format(x))
#        print('The next 9 odd integers are:')
        for i in range(x, x+18, 2):
            print(i, end=', ')
        print(x+18)
    else:
        print("This isn't in integer... you twat.")

if __name__ == '__main__':
    y = float(input('Please enter an integer: '))
    if y.is_integer() == True:
        z = int(y)
        evenOddVend(z)
    else:
        print('The number you have entered is not an integer.')
