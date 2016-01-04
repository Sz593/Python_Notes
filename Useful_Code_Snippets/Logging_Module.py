#! python3

import logging

#Configure the logging module
logging.basicConfig(level=logging.DEBUG, #filename='myProgramLog.txt',
        format=' %(asctime)s - %(levelname)s - %(message)s')
    #The basicConfig level is the minimum level of logging function to show.
    #There are 5 levels, and they're each shown below. If you change the level
    # to level=logging.ERROR, only error and critical messages will display.
    #Use the filename= to write the log to a file instead of displaying it.


#Levels of Logging
logging.debug('Some debugging details.')                    #Logging level 1
logging.info('The logging module is working.')              #Level 2
logging.warning('An error message is about to be logged.')  #Level 3
logging.error('An error has occurred.')                     #Level 4
logging.critical('The program is unable to recover.')       #Level 5

#Disabling Logging
#logging.disable(logging.CRITICAL)
    #This disables logging for all messages at or below the mentioned level


#Example program using logging module debug
logging.info('Start of program factorial program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.info('End of factorial (%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')



