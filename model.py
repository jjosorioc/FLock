import os
from distutils.dir_util import copy_tree
from pathlib import Path
import shutil
import string
import random
from tkinter import Tk, filedialog



def startApp(originalPath: str) -> None:
    """Encrypts all files and subdirectories

    Args:
        originalPath (str): Path to directory, it's name won't be changed.
    """
    try:
        os.chdir(originalPath)
        for dirpath, dirnames, filenames in os.walk(originalPath, topdown=False): # topdown has to be false

            
            for file in filenames:
                
                changeFileName(os.path.join(dirpath, file).replace("\\", "/"), file)
            for direc in dirnames:
    
                changeDirName(dirpath, direc)
    except IOError:
        print("ERROR: Can't seem to find the given file.")
        


def changeFileName(fullPath: str, fileName: str) -> None:
    """Changes the name of the file

    Args:
        fullPath (str): Directory of the file
        fileName (str): Original name of the file
    """

    fullPath = Path(fullPath).as_posix()
    
    newName = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(100))

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

    newDirName = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(100))

    pathWithFolderName = fullPath + "/" + folderName # Original path

    newPathWithDirName = fullPath + "/" + newDirName # New path

    os.mkdir(newPathWithDirName) # Create new folder with new name

    try:
        copy_tree(pathWithFolderName, fullPath + "/" +newDirName) # copy everything inside of original path
    except FileNotFoundError:
        pass

    # Delete original path
    shutil.rmtree(pathWithFolderName)



def showWelcomeMessage() -> None:
    
    root = Tk()
    root.withdraw()
    folderPath = filedialog.askdirectory()
    
    startApp(folderPath)



showWelcomeMessage()
