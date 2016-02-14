README!

Quick start example guide:
1) Unzip the WaifuCollage-JPEG-Resizer.zip file into a directory of your choosing, easiest would be in 'Documents' or 'Downloads'
2) Open the WaifuCollage-JPEG-Resizer folder and open up the rawfiles folder.  THIS IS WHERE YOU WILL PUT ALL THE PHOTOS!
3) You will note the example pictures (not drawn by me); there should be a mix of JPEG and PNG files.  You will convert everything to JPEG format.
4) Open up the commdand line.  You can do this by searching for 'cmd'
5) Change your directory to WaifuCollage-JPEG-Resizer.  If you have unzipped the folder in the 'Downloads' folder, simply type 'cd Downloads', hit enter, then type 'cd WaifuCollage-JPEG-Resizer' and hit enter again. 
It's possible that the WaifuCollage-JPEG-Resizer folder may have a slightly different name, so you may need to alter it to something like 'WaifuCollage-JPEG-Resizer-master...
6) In the command line (black box), type 'WaifuCollageJPEG.exe rawfiles' and hit enter.  Open the processedImg folder and you will find that all the files now have the JPEG/JPG extension!
7) In the command line (black box), type 'WaifuCollageResizer.exe resized' and hit enter.  Open the resized folder and you will find scaled down versions of all the files!

You may wish to make backups of the photos before putting them all in the 'rawfiles' folder and using the program--it has never caused problems in my hands, but just to be safe...

I will be working on the actual collage maker script and should finish it in a few hours.

ADVANCED SETTINGS:
I have hard-coded the 4:3 aspect ratio and don't expect you will need to change it.  I *did* code in the pixel size of each thumbnail to be 136 pixels wide by 102 pixels tall, and can very easily change that (I need to modify the source *.py files)