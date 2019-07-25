# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 07:32:12 2015

@author: SZahn
"""


def roots(a, b, c):
    '''Calculate the roots of a quadratic equation.'''
    D = ((b**2) - (4 * a * c))**0.5
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)

    print('x1 is: {0}'.format(x_1))
    print('x2 is: {0}'.format(x_2))


if __name__ == '__main__':
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    roots(float(a), float(b), float(c))
