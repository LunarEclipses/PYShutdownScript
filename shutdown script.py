import time
import os
i = 0
for i in range(10): 
    while(1 < 10):
        print(10)
        time.sleep(1)
        i = i + 1
        print(9)
        mjbbyh = input("are you sure you want to continue?")
        if (mjbbyh == "yes"):
            i = i + 1
            print(8)
            time.sleep(1)
            i = i + 1
            print(7)
            time.sleep(1)
            i = i + 1
            print(6)
            time.sleep(1)
            i = i + 1
            print(5)
            c = input("are you sure?")
            i = i + 1
            if (c == "yes"):
                print(4)
                print("you have reached the point of no return")
                i = i + 1
                time.sleep(1)
                print(3)
                i = i + 1
                time.sleep(1)
                print(2)
                i = i + 1
                time.sleep(1)
                print(1)
                i = i + 1
                time.sleep(1)
            elif c != "yes":
                quit()
        elif mjbbyh != "yes":
            quit()
        
        
    if(i == 10):
        os.system("shutdown /s /t 1")
