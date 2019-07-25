# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:34:09 2015

@author: SZahn
"""


def printMenu():
    ''' Allows to user to specify how to use the program. '''
    print('1. Convert miles to kilometers')
    print('2. Convert kilometers to miles')


def convMilesToKm():
    '''Converts distance in miles to kilometers.'''
    miles = float(input('Please enter your distance in miles: '))
    km = miles * 1.609
    print('This is {0} kilometers.'.format(km))


def convKmToMiles():
    '''Converts distance in kilometers to miles.'''
    km = float(input('Please enter your distance in kilometers: '))
    miles = km / 1.609
    print('This is {0} miles.'.format(miles))


if __name__ == '__main__':
    printMenu()
    usrInput = int(input('Please select a number: '))
    if usrInput == 1:
        convMilesToKm()
    if usrInput == 2:
        convKmToMiles()
