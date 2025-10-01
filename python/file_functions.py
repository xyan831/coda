# file functions
# xyan831

import os
import re

def cleanout(directory):
    """
    remove all files and folders in directory
    """
    files = os.listdir(directory)
    for item in files:
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            cleanout(path)
            os.rmdir(path)
        else:
            os.remove(directory+'\\'+item)

def filetype_remove(directory, endtype):
    """
    remove all files of same type in directory
    """
    for filename in os.listdir(directory):
        if filename.endswith(endtype):
            path = os.path.join(directory,filename)
            #print(filename)
            os.remove(path)

def multifile_rename(directory, oldtxt, newtxt):
    """
    rename multiple files in directory
    replace old text with new text in filename
    """
    for filename in os.listdir(directory):
        if oldtxt in filename:
            newname = filename.replace(oldtxt,newtxt,1)
            #print(filename)
            #print(newname)
            os.rename(os.path.join(directory, filename), os.path.join(directory, newname))

def find_btw(mark, txt):
    """
    find text btw 2 markers
    mark = markers [start, end]
    lst = list of all text btw markers
    """
	pat = re.compile(mark[0]+'(.*?)'+mark[1], re.S)
	find_list = pat.findall(txt)
	return find_list

if __name__ == "__main__":
    # cleanout downloads folder
    directory1 = "path/to/downloads"
    #cleanout(directory1)
    
    # mass rename files
    directory2 = "path/to/directory"
    folder2 = "folder"
    path2 = os.path.join(directory2, folder2)
    #multifile_rename(path2)
    
    # remove all .bak files
    directory3 = "path/to/folder"
    #filetype_remove(directory3, ".bak")

