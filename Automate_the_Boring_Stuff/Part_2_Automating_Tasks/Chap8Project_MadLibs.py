#!  python3

import os, re

# Make sure we're in the correct directory
os.chdir('C:\\PythonScripts\\Automate_the_Boring_Stuff\\'
            'Part_2_Automating_Tasks')

# Open the mad libs file and read the content
madLibs = open('MadLibs_Example.txt','r')
madLibsText = madLibs.read()

# Create a regex to find all adjectives, nouns, and verbs
foo = re.compile(r'ADJECTIVE|NOUN|VERB')
items = foo.findall(madLibsText)
print(items)
for i in items:
    if str(i).lower() == 'adjective':
        print('Enter an adjective:')
    else:
        print('Enter a ' + str(i).lower() + ':')
    usrInput = input()
    madLibsText = foo.sub(usrInput,madLibsText,count=1)

print(madLibsText)
