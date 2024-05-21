import itertools
import string

size=int(input("Enter the size of the password : "))

name=input("Enter the name of your file : ")

YourCharacterList=input("Enter your character list : ")

file=open(name+".txt","a+")
text=itertools.product(YourCharacterList,repeat=size)
for x in text:
    file.write("".join(x))
    file.write("\n")


