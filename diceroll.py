import random
import time

# Function for enabling the simulation of a dice roll.
def rollthedice():
    for player_no in range(1,7):
        number = random.randint(1,6)
        print(f"For player number {player_no}, the number is {number}")
        time.sleep(2)



print("This is a Dice Roll Simulator !! ")
done=True
while done:
    rollthedice()
    print("\nWould you like to continue")
    state=input("Enter 1 for Yes and 0 for No !!  ")
    if state=='1':
        continue
    else:
        done=False
        
print("\nHere it is the end of the Simulation. \n")