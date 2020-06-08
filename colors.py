import os 
import sys
import time
os.system ("figlet Color")
green = "\033[1;32;40m Bright Green  \n"
red = "\033[1;31;40m Red \n"
blue = "\033[1;34;40m Blue\n"
yellow = "\033[1;33;40m Yellow\n"
purple ="\033[1;35;40m Purple\n"
cyan = "\033[1;36;40m Cyan\n"
gray = "\033[1;30;40m Gray\n"
print ("1: Green") 
print ("2: Red")
print ("3: Blue")
print ("4: Yellow")
print ("5: Purple")
print ("6: Cyan")
print ("7: Gray")
Color = input ("Enter a number: ")
if Color == 1:
         print (green)
elif Color == 2:
          print (red)
elif Color == 3:
           print (blue)
elif Color ==4:
            print (yellow)
elif Color ==5:
             print (purple)
elif Color ==6:
              print (cyan)
elif Color ==7:
               print (gray)
else:
       print ("Wrong")
os.system ("clear")







       
        
