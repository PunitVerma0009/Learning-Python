import random
l=['Stone','Paper','Scissor']
print(" Lets play Stone,Paper and Scissor-> \n Remember if you want to exit just press e")
me=0
com=0
dr=0
while(True):
    userInput=input("Enter your choice=").capitalize()
    if userInput=="E":
        print(f'total scores= \n you={me} \n computer={com} \n draw={dr}')
        if me>com:
            print("    Overall you win     ")
        elif me<com:
             print("    Overall you lose     ")   
        else:
            print("    Overall draw     ")      
        print("exiting game.....")
        break
    else:
        computerOut=random.choice(l)
        print("computer output=",computerOut)
        if userInput=="Stone":
            if computerOut=="Stone":
                print("      Draw🙃     ")
                dr=dr+1
            elif computerOut=="Paper":
                print("    You Lose🥺    ")
                com=com+1
            else:
                print("   You Win😄     ")
                me=me+1    
        elif userInput=="Paper": 
            if computerOut=="Stone":
                print("   You Win😄     ")
                me=me+1 
            elif computerOut=="Paper":
                print("      Draw🙃     ")
                dr=dr+1
            else:
                print("    You Lose🥺    ")
                com=com+1  
        elif userInput=="Scissor":
            if computerOut=="Stone":
                print("    You Lose🥺    ")
                com=com+1
            elif computerOut=="Paper":
                print("   You Win😄     ")
                me=me+1 
            else:
                print("      Draw🙃     ")
                dr=dr+1  
        else:
            print("Invalid input please enter a valid input")  