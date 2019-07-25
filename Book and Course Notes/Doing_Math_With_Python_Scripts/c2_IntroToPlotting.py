# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:00:15 2015

@author: SZahn
"""


import matplotlib.pyplot as plt


def createGraph():
    x_numbers = [1, 2, 3]
    y_numbers = [2, 4, 6]

    plt.plot(x_numbers, y_numbers)
    plt.show()


if __name__ == '__main__':
    createGraph()
