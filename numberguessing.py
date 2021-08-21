import random
import time
time.sleep(2)
print("This is a Game!!")
print("This is a Number Guessing game.")
time.sleep(2)
print("The rules are pretty Simple")
time.sleep(4)
print("You get 3 chances to guess the number!!")
print("The range is between 1 to 10")
print("Every time you guess 'WRONG' your chances decline!")
print("Let's Start!!")
number=random.randint(1,10)
for i in range(3):
    time.sleep(4)
    user=int(input("Guess a number: "))
    if user==number:
        print("Hurrah!!! You guessed it right!!!")
        print(f"The number you guessed is correct and it is {number}")
        break
    elif user>number:
        print("WRONG GUESS!!!!!!!!You are too far from the number")
        print("Try once again!!")
    else:
        print("WRONG GUESS!!!!!!!You are too low to the number")
        print("Try once again!!")
else:
    print(f"Better Luck next time!!, The number is {number}")