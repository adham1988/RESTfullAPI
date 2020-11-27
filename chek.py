import time
import os
from datetime import datetime

def add_to_logfile(my_list):   #function to add logfile
    d = datetime.now()
    with open('log.txt', 'a+') as f:
        f.write(d.strftime('%Y-%m-%d %H:%M:%S') + " Rule = " + "%s" % my_list[len(my_list)-1] + "\n")
    f.close()        

liste = []


while(True):
    
    print(liste)
    if ((os.stat("file.txt").st_size == 0)==False):
        with open("file.txt") as fa:
            lines = fa.readline()
            print("here is line")
            print(lines)
            liste.append(lines)
        open('file.txt', 'w').close()
        print(liste)
        add_to_logfile(liste)
        print("Send commando to actuator")

    time.sleep(2)




