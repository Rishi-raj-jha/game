 # PROJECT 2 – THE PERFECT GUESS
 
 
 
import random
n = random.randint(1, 100)
a = -1
guess = 0

while a != n:
    num = int(input("Guess the number :- "))
    guess += 1  # increment attempt count

    if num > n:
        print("Lower number please!")
    elif num < n:
        print("Higher number please!")
    else:
        print(f"You have guessed the number {n} correctly in {guess} attempts. Thank you for playing this game!")
        print(f"Debug: Current guess count = {guess}")