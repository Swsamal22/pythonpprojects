import random
from wordlist import words

word=random.choice(words)

chances=6
guesses=[]
done=False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("*", end=" ")
    print("")
    done=True
    
    guess=input(f"Allowed chances {chances}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break
    
    done=True
    for letter in word:
        if letter.lower() not in guesses:
            done=False
        
        
if done:
    print(f"You have found the word! it was {word}! ")
else:
    print(f"Game over! The word was {word}")