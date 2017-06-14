import time
import webbrowser

def break_time():
    
    print ("The program startd on:"+time.ctime())

    for i in range(0,5):
        time.sleep(5)
        webbrowser.open("https://www.youtube.com/watch?v=RBumgq5yVrA&list=RDRBumgq5yVrA")
        print ("\n Break No.",i,"\nTime:",time.ctime())

break_time()
