#! python3

import os, re

print('Please enter a regular expression')
regex = input()

print(regex)

foo = re.compile(regex)

for file in os.listdir("C:\\PythonScripts\\Sandbox"):
    if file.endswith(".txt"):
        openFile = open("C:\\PythonScripts\\Sandbox\\" + file,'r')
        for line in openFile:
            print(foo.findall(line))
        openFile.close()
        

