# File-Viewer
A simple console application that allows users to navigate up and down in a text file. 
This function and code that launches it is stored as a main program in a module named view.py. The entire text of the file will not be stored in memory– program will reread portions of the file to display the appropriate text on demand.

First traverses the requested file to determine the file positions where each “page” (screen) begins. Then display the first page, and gives the user the following prompt: Command [u,d,t,b,#,q]:

NOTE: # represents a page number entered by the user, not a pound sign typed by the user.

The commands are interpreted as follows:

u: move up one page; if already at the top, wrap to the last page
d: move down one page; if at the bottom, wrap to the first page
t: move to the top (first) page
b: move to the bottom (last) page
#: moves to page number entered (1-based)
q: quit

If the user just hits the Enter key, it's considered a “down” command. If the user enters a number, move to that page/screen. If the number is out of range, move to the top or bottom, as appropriate. Obtains the file name from the command line when view.py is the top-level module. In addition, processes an optional, second command-line argument that represents the desired screen display size (which defaults to 25).

The file 'Yankee.txt' was used with this program, it has a word count of 18,901.
