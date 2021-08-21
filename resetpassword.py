import random
def resetpassword():
    temp=""
    #list of symbols, letters,numbers that will be used in generating password
    symbol=["~",".","!","@","#","$","%","^","&","*"]
    letter=["q","w","e","r","t","y","u","i","o","p","l","k","j","h","g","f","d","s","a","z","x","c","v","b","n","m"]
    number=["1","2","3","4","5","6","7","8","9","0"]
    for i in range(2):
        temp+=random.choice(letter)
    for i in range(2):
        temp+=random.choice(symbol)
    for i in range(2):
        temp+=random.choice(number)

    return temp
