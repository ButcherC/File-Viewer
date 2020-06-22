# File Viewer
# import statements
from itertools import islice
import sys

def view(fname, view_size = 25):

    length = len(sys.argv)
    # obtain the file name from the command line when view.py is the top
    # level module
    # if sys.argv((len) == 2) then view_size is default

    #if sys.argv((len) == 3) then view size was specified by user
    # process an optional, second command line argument that represents
    # the desired view_size (could be changed to 20 for ex.)
    if(length == 3):
        view_size = sys.argv[4]
    else:
        view_size = view_size
    pos = []
    count = 0
    file_pos = 0
    SEEK_CUR = 1
    # open the file
    #fp = open(fname, 'r')
    # traverse the file to determine the file positions where
    # each 'page' (screen) of view_size lines begins:
   
    with open(fname, 'r') as fp:
        line = fp.readline()
        while(line != ''):
            for i in range(1,view_size):
                fp.readline()
                count +=1
                #file_pos += len(i)
            pos.append(fp.tell())
            line = fp.readline()
            #fp.flush()
            
    i = 0
    lastIndexPosition = len(pos)-1
    print(pos)
    print(count)
    fp = open(fname, 'r')
    fp.seek(i)
    print(fp.read(pos[i]))
        ###pos.append(fp.tell())
    # read view_size lines
    #record the file position by calling file.tell()
    #pos.append(fp.tell())
    # repeat until passed through entire file once while ! eof?
    #display the first page
    # give prompt: Command [u,d,t,b,#,q]:
    # file.seek() is used to move from page to page
    command = None
    while(command != 'q'):
        command = input("Command [u,d,t,b,#,q]: ")
#move up one page
        if((command == 'u') and (i != 0)): 
            fp.seek(pos[i - 1])
            print(fp.read(pos[i]))
            i = i - 1
#if at top wrap to last page
        elif((command == 'u') and (i == 0)): 
            fp.seek(pos[lastIndexPosition - 1])
            print(fp.read(pos[lastIndexPosition]))
            i = lastIndexPosition
# move down one page
        elif(((command == 'd') or (command == '')) and (i != lastIndexPosition)): 
            fp.seek(pos[i])
            print(fp.read(pos[i]))
            i = i + 1
#if at bottom wrap to first page
        elif(((command == 'd') or (command == '')) and (i == lastIndexPosition)): 
            fp.seek(0)
            print(fp.read(pos[0]))
            i = 0
# move to top (first page)
        elif(command == 't'): 
            fp.seek(0)
            print(fp.read(pos[0]))
            i = 0
#move to last page
        elif(command == 'b'): 
            fp.seek(pos[lastIndexPosition - 1])
            for i in range(1,25):
                print(fp.readline())
            i = lastIndexPosition
        elif(command == 'q'):
            fp.close()
# move to page number (1 based)
        else:
            for j in range(1, lastIndexPosition):
                if((command == '#' + str(j)) or (command == '# ' + str(j)) or (command == str(j))):
                    fp.seek(pos[j])
                    print(fp.read(pos[j]))
                    
        


        
    
