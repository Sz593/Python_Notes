# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:00:15 2015

@author: SZahn
"""


import pylab

nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3,
                 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0,
                 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0,
                 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months = range(1, 13)

'''
plot(months, nyc_temp_2000)
plot(months, nyc_temp_2006)
plot(months, nyc_temp_2012)
'''

pylab.plot(months, nyc_temp_2000, months, nyc_temp_2006,
           months, nyc_temp_2012)
pylab.title('Average Monthly Temperature in NYC')
pylab.xlabel('Month')
pylab.ylabel('Temperature')
pylab.axis(xmin=1)  # tuble syntax: axis([xmin, xmax, ymin, ymax])
pylab.legend([2000, 2006, 2012])
# show
pylab.savefig('test_graph.pdf')
