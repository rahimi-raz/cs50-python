# Import the pyfiglet module
import pyfiglet as pyg
import sys
import random
f=pyg.FigletFont.getFonts()
try:
    if len(sys.argv)==3:
        if sys.argv[2] in f and sys.argv[1] in ("-f","--font"):
            s=input("")
            print(pyg.figlet_format(s,font=sys.argv[2]))
        else :
             raise IndexError
    elif len(sys.argv)==1:
            s=input("")
            r=random.choice(f)
            print(pyg.figlet_format(s,font=r))
    else:
         raise IndexError
except (IndexError):

