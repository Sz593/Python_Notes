#! python3

import os

def folderSize(folder):
    folderSize = 0
    for (foldername, subfolders, filenames) in os.walk(folder):
        for file in filenames:
            filename = os.path.join(foldername, file)
            folderSize += os.path.getsize(filename)
    return folderSize

print(get_size())