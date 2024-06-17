import os
path=os.chdir("D:\Punit\Python VE\os\data")
# print(os.getcwd())
files=os.listdir(path)
# print(files)
j=1
a=int(input("to encode the files press 1="))
if a==1:
    for i in files:
        if i.endswith(".jpg")==True:
            os.rename(f"{i}",f"{j}.clg")
            j+=1
# print(os.getcwd())
print(os.listdir(path))
a=int(input("to decode the files press 2="))
if a==2:
    for i in files:
        if i.endswith(".clg")==True:
            os.rename(f"{i}",f"{j}.jpg")
            j+=1
# print(os.getcwd())
print(os.listdir(path))