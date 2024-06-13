import random
l=['Stone','Paper','Scissor']
print(" Lets play Stone,Paper and Scissor-> \n Remember if you want to exit just press e")
while(True):
    userInput=input("Enter your choice=").capitalize()
    if userInput=="E":
        print("exiting game.....")
        break
    else:
        computerOut=random.choice(l)
        print("computer output=",computerOut)
        if userInput=="Stone":
            if computerOut=="Stone":
                print("      Draw🙃     ")
            elif computerOut=="Paper":
                print("    You Lose🥺    ")
            else:
                print("   You Win😄     ")    
        elif userInput=="Paper": 
            if computerOut=="Stone":
                print("   You Win😄     ")
            elif computerOut=="Paper":
                print("      Draw🙃     ")
            else:
                print("    You Lose🥺    ")  
        elif userInput=="Scissor":
            if computerOut=="Stone":
                print("    You Lose🥺    ")
            elif computerOut=="Paper":
                print("   You Win😄     ")
            else:
                print("      Draw🙃     ")  
        else:
            print("Invalid input please enter a valid input")  