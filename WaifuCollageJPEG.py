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

def jpegConvert(fname,r,p,name):
    tempImage = Image.open(r+'\\'+fname).convert('RGB')
    tempImage.save(p+'\\'+name+'.jpg')
    

def convertFiles(raw,proc,exists):
    if exists > 0:
        procList = os.listdir(proc)
    for filename in os.listdir(raw):
        dot = filename.find('.')
        rawName = filename[0:dot]
        #extension = filename[dot+1:len(filename)]
        checkName = rawName + '.jpg'
        if exists > 0 and checkName in procList:
            0
        else:
            jpegConvert(filename,raw,proc,rawName)
                

    
"""
MAIN SCRIPT
"""

rawDir = sys.argv[1]
waifuFolder = os.getcwd() + '\\'
fullRawDir = waifuFolder + rawDir

print('The raw image directory you selected is:')
print(fullRawDir)

print('Making processed image folder...')
procImg = waifuFolder + 'processedImg'

""" Convert to *.jpeg """
try:
    os.makedirs(procImg)
    print('Converting filetypes to *.jpg...')
    convertFiles(fullRawDir,procImg,0)
except BaseException:
        print('Processed image folder exists!  Updating...')
        # REMOVE LATER
        convertFiles(fullRawDir,procImg,1)

