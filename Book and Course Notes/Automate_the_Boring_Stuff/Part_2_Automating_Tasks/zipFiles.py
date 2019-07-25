#! python3

import zipfile, os

#Set the directory
defaultFilePath = 'C:\\PythonScripts\\Sandbox'
os.chdir(defaultFilePath)
print('The current directory is: ' + os.getcwd())


#Open zip file
egZip = zipfile.ZipFile('example.zip')


#List of files/folders in zip file
print(egZip.namelist())


#File Information
spamInfo = egZip.getinfo('spam.txt')
print('The regular file size is: ' + str(spamInfo.file_size))
print('The compressed file size is: ' + str(spamInfo.compress_size))
print('Compressed file is %sx smaller!'
      % (round(spamInfo.file_size / spamInfo.compress_size,2)))


#Extract all files from zip
egZip.extractall('ExampleZip')  #creates a new folder called ExampleZip
                                    # and extracts all to the new folder


#Extract a single file from zip
egZip.extract('spam.txt')   #extracts spam.txt into the current directory
egZip.extract('spam.txt','NewFolder') #extracts spam.txt into a newly
                                        #created folder

#Close zip file
egZip.close()


#Create a new zip file
newZip = zipfile.ZipFile('new.zip','w') #'w' specifies write mode. This
                                        #will erase an existing zip file's
                                        #contents. To add to an existing zip
                                        #file, use append mode ('a').

#Write to a new zip file
newZip.write('hello.txt',compress_type=zipfile.ZIP_DEFLATED)
                                        #The ZIP_DEFLATED compression type
                                        #works well with all file types, so
                                        #it's always a good default.
newZip.close()


###Optional File Cleanup!
##import send2trash
##
##send2trash.send2trash('spam.txt')
##send2trash.send2trash('NewFolder')
##send2trash.send2trash('ExampleZip')
##send2trash.send2trash('new.zip')
