# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:03:32 2015

@author: SZahn
"""

import matplotlib.pyplot as plt


def draw_graph(x, y):
    '''Plot the graph of F(r)'''
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance (m)')
    plt.ylabel('Gravitational Force (N)')
    plt.title('Gravitational Force As a Function of Distance')
    plt.show()


def generate_F_of_r(m1, m2):
    '''Generate values for F(r) at distance intervals.'''
    distance = range(100, 1001, 50)
    F = []
    G = 6.674*(10**-11)

    for r in distance:
        F_calc = (G * m1 * m2) / (r**2)
        F.append(F_calc)

    draw_graph(distance, F)


if __name__ == '__main__':
    mass1 = float(input('First mass in kg: '))
    mass2 = float(input('Second mass in kg: '))
    generate_F_of_r(mass1, mass2)
