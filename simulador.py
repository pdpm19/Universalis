# Main file
# Standard imports
import os
import sys

workingDirectory = os.getcwd()
accessPath = os.path.join(workingDirectory, 'access')
dbPath = os.path.join(workingDirectory, 'db')
uiPath = os.path.join(workingDirectory, 'gui')
seleniumPath = os.path.join(workingDirectory, 'selenium')

sys.path.append(accessPath)
sys.path.append(dbPath)
sys.path.append(uiPath)
sys.path.append(seleniumPath)

# My imports
from gui import GUILoad

if __name__ == '__main__':
    # 1. Checks if everything is OK

    # 2. Calls the GUI
    paths = [uiPath, accessPath, dbPath, seleniumPath]
    GUILoad(paths) 
