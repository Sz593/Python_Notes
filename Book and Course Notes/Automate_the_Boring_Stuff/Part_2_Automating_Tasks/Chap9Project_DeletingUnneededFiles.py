#! python3

import os, send2trash

def folderSize(folder):
    folderSize = 0
    for (foldername, subfolders, filenames) in os.walk(folder):
        for file in filenames:
            filename = os.path.join(foldername, file)
            folderSize += os.path.getsize(filename)
    return folderSize

def humanSize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    if nbytes == 0: return '0 B'
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

def itemSize(folder):
    folder = os.path.abspath(folder)
    print('The following folders and files are 100 MB (100,000 bytes) '
          ' or larger.')
    
    for foldername, subfolders, filenames in os.walk(folder):
##        print('The current folder being searched is: ' + foldername)

        if folderSize(foldername) > 100000000:
            print(foldername +' is ' +
                  humanSize(folderSize(foldername)) + ' (' +
                  str(folderSize(foldername)) + ' bytes).')
            print('')

##        for subfolder in subfolders:
##            if folderSize(str(folder + os.sep + subfolder)) > 100000000:
##                print('    Subfolder of ' + foldername + ': ' + subfolder +
##                      ' is ' + humanSize(folderSize(str(folder + os.sep +
##                                         subfolder))) + ' (' + str(
##                        folderSize(str(folder + os.sep + subfolder))) +
##                      ' bytes).')
##                print('')
            
        for file in filenames:
            if os.path.getsize(foldername + os.sep + file) > 100000000:
                print('File inside ' + foldername + ': ' + file + 
                      ' is ' + humanSize(os.path.getsize(foldername +
                                                   os.sep + file)) + ' (' +
                      str(os.path.getsize(foldername + os.sep + file)) +
                      ' bytes).')
                print('')

    print('Searching complete.')

print('Please choose a folder.')
usrFolder = input()

itemSize(usrFolder)
