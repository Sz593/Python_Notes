#! python3

import re

def regexStrip(text,delimiter):
    foo = re.compile(r'^\s*(\w+)(\s?\w+)*\s*$')
    bar = foo.sub(r'\2\3',text)
    return bar

print('What is your text?')
usrInput = str(input())

print(regexStrip(usrInput,'foo'))
