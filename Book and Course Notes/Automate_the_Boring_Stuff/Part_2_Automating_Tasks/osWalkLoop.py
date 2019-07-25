#! python3

import os

os.chdir('C:\\PythonScripts\\Sandbox')

for folderName, subfolders, files in os.walk(os.getcwd()):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print ('Subfolder of ' + folderName + ': ' + subfolder)
    for filename in files:
        print ('File inside ' + folderName + ': ' + filename)
    print('')
