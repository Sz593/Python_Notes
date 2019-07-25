#! python3

# backupToZip.py - copies an entire filder and its contents into a zip
#   file whose filename increments.

import zipfile, os

def backupToZip(folder):
    """ Backs up a folder to a zip file

    This function takes the contents (recursively) of a folder and backs
    them up to a zip file."""

    folder = os.path.abspath(folder)    #Ensure we're using the absolute path
    number = 1

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    #Create the zip file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w')

    #Walk the directory tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))

        #Add current folder to the zip file
        backupZip.write(foldername)

        #Add all files in this folder to the zip file
        for file in filenames:
            newBase = os.path.basename(folder) + '_'
            if file.startswith(newBase) and file.endswith('zip'):
                continue #Don't back up zip files
            backupZip.write(os.path.join(foldername, file))
    backupZip.close()
    print('Done.')


print('Please select a folder (absolute path)')
usrPath = input()
backupToZip(usrPath)
