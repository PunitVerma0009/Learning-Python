import random
import msvcrt
six=[1,6,2,6,3,6,4,6,5,6,6,6]
one=[1,1,1,2,1,3,1,4,1,5,1,6]
two=[2,1,2,2,2,3,2,4,2,5,2,6]
while True:
    choose=input("Which dice do you want to choose=\n 0=unbiased dice\n 1=(1)biased dice\n 2=(2)biased dice\n 6=(6)biased dice \n E=exit \n=")
    if choose=="0":
        print("Press E to exit \n Else press enter")
        while True:
            b=msvcrt.getwch()
            if b=="E" or b=="e":
                print("Geting back...........")
                break
            else:
                print(random.randint(1,6))
    elif choose=="1":
        print("Press E to exit \n Else press enter")
        while True:
            b=msvcrt.getwch()
            if b=="E" or b=="e":
                print("Geting back.........")
                break
            else:        
                print(random.choice(one))
    elif choose=="2":
        print("Press E to exit \n Else press enter")
        while True:
            b=msvcrt.getwch()
            if b=="E" or b=="e":
                print("Geting back.........")
                break
            else:        
                print(random.choice(two))
    elif choose=="6":
        print("Press E to exit \n Else press enter")
        while True:
            b=msvcrt.getwch()
            if b=="E" or b=="e":
                print("Geting back.........")
                break
            else:        
                print(random.choice(six))
    elif choose=="E" or choose=="e": 
        print("Exiting..........")
        break
    else:
        print("Invalid input")               