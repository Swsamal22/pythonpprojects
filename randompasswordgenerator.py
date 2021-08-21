import random
#defining a function which wil combine the letters, numbers and symbols
def generator(sym,let,num):
    temp=""
    s=let+num+sym
    temp+=s
    return temp


#list of symbols, letters,numbers that will be used in generating password
symbol=["~",".","!","@","#","$","%","^","&","*"]
letter=["q","w","e","r","t","y","u","i","o","p","l","k","j","h","g","f","d","s","a","z","x","c","v","b","n","m"]
number=["1","2","3","4","5","6","7","8","9","0"]
x=input("Enter your username: ")

#extracting the first 4 charecters of the username for a better password
y=x[:4]
A=""
while len(A)<5:
    sym,let,num=random.choice(symbol),random.choice(letter),random.choice(number)
    A+=generator(sym,let,num)


#password is combination of the user name and randomly generated charecters
password=y+A
print(password)
