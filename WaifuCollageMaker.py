# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:29:26 2016

@author: AkemiHomuraLover

Directions:

syntax:
USE PYTHON 2.7!
1) Move WaifuCollage.py into a directory of your choosing; make sure you have enough disk space
2) Make a folder named 'rawfiles'
3) Please place all raw image files into 'rawfiles' folder

4) cd \Path\to\script\
5) python WaifuCollage.py rawfiles


"""


""" VARIABLES TO CHANGE """


""" OPTIONS """
AUTO_FIT = 1 #Performs autoFit
RESIZE = 1 #Performs resize
STANDARD_WIDTH = 400
STANDARD_HEIGHT = 300
""" Packages """
import sys
import os
import scipy
from PIL import Image
import shutil
import csv
"""
HELPER FUNCTIONS
"""



# Since we use a numbering system and what are essentially thumbnails, it is less-confusing, albeit less efficient, to simply redo this process eveyr time the program is run.

def enumerator(source,out):
    counter = 0
    for filename in os.listdir(source):
        counter = counter+1
        newName = str(counter)
        tempImage = Image.open(source+'\\'+filename)
        tempImage.save(out+'\\'+newName+'.jpg')
            

def collageMaker(path,output,data):
    nFiles = len(os.listdir(path))
    nRows = len(data)
    nCols = len(data[0])
    nColsLast = len(data[nRows-1])
    STANDARD_COLS = len(data[0])
    # http://stackoverflow.com/questions/4567409/python-image-library-how-to-combine-4-images-into-a-2-x-2-grid
    new_size = (int(STANDARD_WIDTH*STANDARD_COLS), int(STANDARD_HEIGHT*nRows))
    new_im = Image.new("RGB", new_size)
    heightAdjust = 0
    counter = 0
    allFiles = os.listdir(path)
    for i in range(nRows - 1):
        widthAdjust = 0
        temp = []
        for j in range(nCols):
            tempImage = Image.open(path+'\\'+data[i][j]+'.jpg')
            new_im.paste(tempImage, (widthAdjust,heightAdjust))
            widthAdjust = widthAdjust + STANDARD_WIDTH
        heightAdjust = heightAdjust + STANDARD_HEIGHT
    widthAdjust = 0
    temp = []
    for k in range(nColsLast):
        if len(data[nRows-1][k]) > 0:
            tempImage = Image.open(path+'\\'+data[nRows-1][k]+'.jpg')
            new_im.paste(tempImage, (widthAdjust,heightAdjust))
            widthAdjust = widthAdjust + STANDARD_WIDTH
    new_im.save(output+'\\'+'collage.jpg')

    
def makeCollage(path):
    collageAssembler(path,0)
    #http://stackoverflow.com/questions/16179875/command-line-input-in-python
    user_input = raw_input("Rearrange filenames in collage folder as necessary.  Hit Enter to continue...")
    os.remove(path+'\\'+'collage.jpg')
    collageAssembler(path,1)
    user_input = raw_input("Please stash the collage.csv file somewhere safe for recordkeeping.  You may wish to give it a better name.  Hit Enter to finish...")
    
"""
MAIN SCRIPT
"""

resizerDir = sys.argv[1]
outputDir = sys.argv[2]
waifuFolder = os.getcwd() + '\\'
fullResizerDir = waifuFolder + resizerDir
fullOutputDir = waifuFolder + outputDir

print('The source image directory you selected is:')
print(fullResizerDir)

        
""" ENUMERATION """
numImg = waifuFolder + 'enumerated'
try:
    os.makedirs(numImg)
    print('Performing image enumeration...')
    enumerator(resizeImg,numImg)
except BaseException:
    print('Enumerated folder exists!  Updating...')
    shutil.rmtree(numImg)
    os.makedirs(numImg)
    enumerator(fullResizerDir,numImg)

""" NOW ONTO THE ACTUAL COLLAGE-MAKING! """    

""" Handles the master grid """
collageImg = waifuFolder + 'output'
overlord = waifuFolder + 'CollageMap.csv'
with open(overlord, 'r') as csvfile:
    traceOn = csv.reader(csvfile, delimiter=',')
    unlimitedBladeWorks = []
    for row in traceOn:
        unlimitedBladeWorks.append(row)


try:
    os.makedirs(collageImg)
    print('Performing collage making...')
    collageMaker(numImg,collageImg,unlimitedBladeWorks)
except BaseException:
    print('Collage image folder exists!  Updating...')
    shutil.rmtree(collageImg)
    os.makedirs(collageImg)
    collageMaker(numImg,collageImg,unlimitedBladeWorks)