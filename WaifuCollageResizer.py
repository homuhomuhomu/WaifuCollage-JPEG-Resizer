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
STANDARD_RATIO = 4.0/3.0 #width:height
STANDARD_WIDTH = 400 #pixels
STANDARD_HEIGHT = int(STANDARD_WIDTH * 1/STANDARD_RATIO)


""" OPTIONS """
AUTO_FIT = 1 #Performs autoFit
RESIZE = 1 #Performs resize

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
    

def scaler(fname,r,name,output):
    tempImage = Image.open(r+'\\'+fname)
    size = STANDARD_WIDTH, STANDARD_HEIGHT
    # http://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
    tempImage.thumbnail(size,Image.ANTIALIAS)
    tempImage.save(output+'\\'+name+'_RESIZE.jpg')

    
def resize(res,exists,output):
    if exists > 0:
        resList = os.listdir(res)
    for filename in os.listdir(res):
        dot = filename.find('.')
        autoName = filename[0:dot]
        checkName = autoName + '_RESIZE.jpg'
        if exists > 0 and checkName in resList:
            0
        else:
            scaler(filename,res,autoName,output)


    
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

        
""" RESIZER """
if RESIZE == 1:
    resizeImg = waifuFolder + resizerDir
    try:
        os.makedirs(fullOutputDir)
        print('Performing Resize...')
        resize(resizeImg,0,fullOutputDir)
    except BaseException:
        print('Resize image folder exists!  Updating...')
        resize(resizeImg,1,fullOutputDir)
        
