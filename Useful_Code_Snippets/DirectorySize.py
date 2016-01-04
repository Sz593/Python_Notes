#! python3

import os

def dirSize(pth = '.'):
    '''
    Prints the size in bytes of a directory.

    This function takes the current directory by default, or the path specified
    and prints the size (in bypes) of the directory. 
    '''
    totSize = 0
    for filename in os.listdir(pth):
        totSize += os.path.getsize(os.path.join(pth, filename))
    return totSize

print('Your current directory is ' + os.getcwd())
print('What is the file path you want to look at?')
foo = str(input())

print(dirSize(foo))
