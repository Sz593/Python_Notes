#! python3

#renameDates.py - Renames filenames with American-style MM-DD-YYYY dates
#to European-style DD-MM-YYYY dates.

import shutil, os, re

datePattern = re.compile(r'''^(.*?) #All text before the date
    ((0|1)?\d)-                     #one or two digits for the month
    ((0|1|2|3)?\d)-                 #one or two digits for the day
    ((19|20)\d\d)                   #four digits for the year
    (.*?)$                          #all text after the date
    ''',re.VERBOSE)

#Move to directory
print("Which directory would you like to use?")
usrDir = input()
os.chdir(usrDir)

#Loop over files in CWD
for usaFile in os.listdir('.'):
    foo = datePattern.search(usaFile)

    #Skip files without a date
    if foo == None:
        continue

    #Get different parts of the filename
    beforeDate = foo.group(1)
    dateMonth = foo.group(2)
    dateDay = foo.group(4)
    dateYear = foo.group(6)
    afterDate = foo.group(8)
    
    #Form the European-style dates
    euFile = beforeDate + dateDay + '-' + dateMonth + '-' + dateYear + \
        afterDate

    #Get the absolute file paths
    absWorkingDir = os.path.abspath('.')
    usaFile = os.path.join(absWorkingDir, usaFile)
    euFile = os.path.join(absWorkingDir, euFile)

    #Rename the files
    print('Renaming "%s" to "%s"...' % (usaFile, euFile))
    shutil.move(usaFile, euFile)
