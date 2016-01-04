#! python3

import re

def pwCheck(pw):
    foo = 0
    if len(pw) < 8:
        print('Weak - password too short.')
    else:
        foo += 1
        
    capRegex = re.compile(r'^.*[A-Z].*$')
    if capRegex.search(pw) == None:
        print('Weak - no capital letters.')
    else:
        foo += 1

    lowRegex = re.compile(r'^.*[a-z].*$')
    if lowRegex.search(pw) == None:
        print('Weak - no lowercase letters.')
    else:
        foo += 1

    numRegex = re.compile(r'^.*[0-9].*$')
    if numRegex.search(pw) == None:
        print('Weak - no digits.')
    else:
        foo += 1

    if foo == 4:
        print('The password is strong with this one...')
    else:
        print('Weakling...')

print('Please enter your password:')
password = str(input())

pwCheck(password)
