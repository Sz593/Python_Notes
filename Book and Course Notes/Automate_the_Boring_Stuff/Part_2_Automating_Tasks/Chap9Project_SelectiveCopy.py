#! python3

import os, shutil

def selCopy(currFolder,newFolder,ext):
    currFolder = os.path.abspath(currFolder)
    os.chdir(currFolder)
    
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)
    newFolder = os.path.abspath(newFolder)
    
    for foldername, subfolders, filenames in os.walk(currFolder):
        if foldername == newFolder:
            continue

        print('The current folder is: ' + foldername)

        for subfolder in subfolders:
            print('    Subfolder of ' + foldername + ': ' + subfolder)

        for file in filenames:
            print('    File inside ' + foldername + ': ' + file)
            if file.endswith(ext):
                fileLoc = foldername + os.sep + file
                print('        Copying file to ' + newFolder + os.sep + file)
                shutil.copy(fileLoc,newFolder)

        print('')
    print('Copying complete.')


print('Please select the current folder')
currLoc = input()
print('Please choose a folder to copy files to')
newLoc = input()
print('Please choose a file extension (e.g. .txt). You should '
      'include the dot in typing the extension')
usrExt = input()

selCopy(currLoc,newLoc,usrExt)
