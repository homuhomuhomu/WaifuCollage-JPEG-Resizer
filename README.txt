README!

Quick start example guide:
1) Unzip the WaifuCollage-JPEG-Resizer.zip file into a directory of your choosing, easiest would be in 'Documents' or 'Downloads'
2) Open the WaifuCollage-JPEG-Resizer folder and open up the rawfiles folder.  THIS IS WHERE YOU WILL PUT ALL THE PHOTOS!
3) You will note the example pictures (not drawn by me); there should be a mix of JPEG and PNG files.  You will convert everything to JPEG format.
4) Open up the commdand line.  You can do this by searching for 'cmd'
5) Change your directory to WaifuCollage-JPEG-Resizer.  If you have unzipped the folder in the 'Downloads' folder, simply type 'cd Downloads', hit enter, then type 'cd WaifuCollage-JPEG-Resizer-Maker-master' and hit enter again. 
It's possible that the WaifuCollage-JPEG-Resizer folder may have a slightly different name, so you may need to alter it to something like 'WaifuCollage-JPEG-Resizer-Maker-master...
6) In the command line (black box), type 'WaifuCollageJPEG.exe rawfiles' and hit enter.  Open the processedImg folder and you will find that all the files now have the JPEG/JPG extension!
7) In the command line (black box), type 'WaifuCollageResizer.exe rawfiles resized' and hit enter.  Open the resized folder and you will find scaled down versions of all the files!

You may wish to make backups of the photos before putting them all in the 'rawfiles' folder and using the program--it has never caused problems in my hands, but just to be safe...

***UPDATE 2/14/2016 00:32 EST ***
8) Inside of the WaifuCollage-JPEG-Resizer-Maker-master, you will find a file entitled CollageMap.csv.  You will need to edit its contents but a) DO NOT MOVE IT and b) DO NOT LET EXCEL CHANGE IT TO AN .xlsx or .xls FILE!  IT *MUST* BE A .csv FILE!!!
The general idea is that the program will take all the files from 7, clone them to a directory named 'enumerated' and reassign them numbers as names: 1.jpg, 2.jpg, 3.jpg, etc.
The CollageMap.csv is a table of, as you may have guessed, numbers.  You simply type the number/filename in the position you want it to be.  It's currently in a format where you *MUST* have it shaped like a box (no funky heart shapes, sorry), although
the last row of the box can be a little 'short'.

OK example:
1, 2, 3
4

OK example:
1, 2
3, 4
5

NOT OK example:
1, 2
3,
4, 5

It will probably be easier to understand by running the program and observing the output.  One thing to note, however, is that the 'enumerated' and 'output' folders are essentially deleted every time the Maker script is run, so if you have a product you really
like, you may wish to ferret it away.  The numbers are arranged based on the filename, 'a'b before 'b', '1' before '2', so the numbers *WILL* shift as you add new files to the folder.  
It shouldn't be a big deal unless dealing with 'double' images, i.e. a pair of 400 x300 which stack to make a 400 x 600, inwhich case arrangement on the .csv matters.  I would advise to just run the program once to see how the images are numbered, then
make swaps as necessary (will be clear later)

LET'S TRY IT!
9) Continuing where we left off at 7), punch in 'WaifuCollageMaker.exe resized enumerated' and hit enter
10) Open up the enumerated folder; you will see, surprise, enumerated images from the resized folder
11) Now, open up the output folder.  You will notice that you now have a collage, which takes the form of the CollageMap.csv!  
12) To deal with dubs (pair of stacked 400 x 300), note the numbering in the enumerated folder and change the numbering the the CollageMap.csv to make them fit.  I think it works, but if it doesn't bug me.  I will be on the threads, and I still need to upload
my contribution later anyway.  Here's an example:

Let's say, 18.jpg and 19.jpg are the head and body of Mami respectively, and the current format of the sheet is to extend 10 columns.  Thus, we see:
...
...18, 19, 20
...28, 29, 30
...
This won't do!  We want Mami's head in the right place!  Try changing it to:
...
...18,28,21
...19,29,30
...

Observe the diagonal swap; its probably the easiest way to do this without having to shift all the numbers.

ADVANCED SETTINGS:
I have hard-coded the 4:3 aspect ratio and don't expect you will need to change it.  I *did* code in the pixel size of each thumbnail to be 400 pixels wide by 300 pixels tall, and can very easily change that (I need to modify the source *.py files)

TROUBLESHOOTING:
If the program crashes, check to make sure you don't have any of the folders open in explorer, specifically the 'enumerated' and 'output' folders.  It will work if you close the windows and try again.
If you get errors in the Maker script, make sure your CollageMap.csv makes sense
If you see an error in line 71 for the Resizer, I apologize, I changed the input command a bit, so you need to have both 'rawfiles' and 'resized' (see the MEGA-COMMAND)

MEGA-COMMAND:
If you are tired or retyping for each entry, just use the following (make sure you are in the correct directory):
WaifuCollageJPEG.exe rawfiles & WaifuCollageResizer.exe resized resized & WaifuCollageMaker.exe resized enumerate