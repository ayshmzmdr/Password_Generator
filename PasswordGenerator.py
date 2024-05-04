import random
import string

letter=int(input("Enter the number of alphabets in your password : "))
number=int(input("Enter the number of digits in your password : "))
symbol=int(input("Enter the number of special symbols in your password : "))

size=letter+number+symbol
low=string.ascii_lowercase
upp=string.ascii_uppercase
alpha=low+upp

symb=["/","%","@","#","$","^","&","*","!"]
keyChoice,locChoice="X","X"


keyChoice=input("Do you want to specify a keyword? Y/N : ")
if keyChoice == "Y":
    keyword=input()
    locChoice=input("Do you want the password to start with the keyword? Y/N : ")
passwordSet=[]
for x in range(number):
    passwordSet.append(random.randint(0,9))
for x in range(symbol):
    passwordSet.append(random.choice(symb)) 
for x in range(letter):
    passwordSet.append(random.choice(alpha))
if locChoice == "Y":
    random.shuffle(passwordSet)
    passwordSet.append(keyword)
elif keyChoice == "Y":
    passwordSet.append(keyword)
    random.shuffle(passwordSet)
elif keyChoice == "N":
    random.shuffle(passwordSet)

password=""

for x in range(0,size):
    password=password+str(passwordSet.pop())
print(password)