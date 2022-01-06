import os
from distutils.dir_util import copy_tree
import shutil
import string
import random



def startApp(originalPath: str) -> None:
    """Encrypts all files and subdirectories

    Args:
        originalPath (str): Path to directory, it's name won't be changed.
    """
    os.chdir(originalPath)
    for dirpath, dirnames, filenames in os.walk(originalPath, topdown=False): # topdown has to be false

        # New name for the folder or file
        for file in filenames:
            
            changeFileName(os.path.join(dirpath, file), file)
        for direc in dirnames:
 
            changeDirName(dirpath, direc)
        


def changeFileName(fullPath: str, fileName: str) -> None:
    """Changes the name of the file

    Args:
        fullPath (str): Directory of the file
        fileName (str): Original name of the file
    """
    newName = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(150))

    try:
        dotIndex = fileName.index(".") # .extension

        newPath = fullPath[:fullPath.rindex("/") + 1] + newName + fileName[dotIndex:] # Dir of the renamed file

        os.rename(fullPath, newPath)
    except ValueError:
        pass



def changeDirName(fullPath: str, folderName: str) -> None:
    """Changes the name of the subdirectory.

    Args:
        fullPath (str): Path of the directory
        folderName (str): Original name of the folder
    """

    newDirName = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(150))

    pathWithFolderName = fullPath + "/" + folderName # Original path

    newPathWithDirName = fullPath + "/" + newDirName # New path

    os.mkdir(newPathWithDirName) # Create new folder with new name

    try:
        copy_tree(pathWithFolderName, fullPath + "/" +newDirName) # copy everything inside of original path
    except FileNotFoundError:
        pass

    # Delete original path
    shutil.rmtree(pathWithFolderName)



MYPATH = "PATH"


startApp(MYPATH)