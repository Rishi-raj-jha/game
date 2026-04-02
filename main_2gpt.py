import random
n = random.randint(1, 100)
guess = 0
num = -1

while num != n:
    num = int(input("Guess the number :- "))
    guess += 1

    if num > n:
        print("Lower number please!")
    elif num < n:
        print("Higher number please!")
    else:
        print(f"You have guessed the number {n} correctly in {guess} attempts. Thank you for playing this game!")