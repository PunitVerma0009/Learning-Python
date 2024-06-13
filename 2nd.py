import random
l=['Stone','Paper','Scissor']
result=[['Draw','Lose','Win'],['Win','Draw','Lose'],['Lose','Win','Draw']]
print(" Lets play Stone,Paper and Scissor-> \n Remember if you want to exit just press e")
me=0
com=0
dr=0
while(True):
    print(" 0 for Stone \n 1 for Paper \n 2 for scissor")
    userInput=input("Enter your choice=")
    if userInput.capitalize()=="E":
        print(f'total scores= \n you={me} \n computer={com} \n draw={dr}')
        if me>com:
            print("    Overall you win     ")
        elif me<com:
             print("    Overall you lose     ")   
        else:
            print("    Overall draw     ")      
        print("exiting game.....")
        break
    elif 0<=int(userInput)<3 :
        computerOut=random.randint(0,2)
        print("computer output=",l[computerOut])
        if result[int(userInput)][computerOut]=="Draw":
            print("      Draw      ")
            dr=dr+1
        elif result[int(userInput)][computerOut]=="Win":
            print("     You Win     ")
            me=me+1
        else:
            print("     You Lose     ")
            com+=1  
    else:
        print("invalid input")         