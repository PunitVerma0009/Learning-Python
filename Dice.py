import random
import msvcrt
l=[1,6,2,6,3,6,4,6,5,6,6,]
while True:
    choose=input("Which dice do you want to choose=\n 1=unbiased dice\n 2=(6)biased dice \n E=exit \n=")
    if choose=="1":
        print("Press E to exit \n Else press enter")
        while True:
            b=msvcrt.getwch()
            if b=="E" or b=="e":
                print("Geting back...........")
                break
            else:
                print(random.randint(1,6))
    elif choose=="2":
        print("Press E to exit \n Else press enter")
        while True:
            b=msvcrt.getwch()
            if b=="E" or b=="e":
                print("Geting back.........")
                break
            else:        
                print(random.choice(l))
    elif choose=="E" or choose=="e": 
        print("Exiting..........")
        break
    else:
        print("Invalid input")               