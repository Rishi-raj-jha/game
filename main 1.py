import random

def game_result(user, computer):
    if user == computer:
        return "It's a Draw"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "You win"
    else:
        return "Computer wins"
    
    
choices = ["snake" , "water","gun"]

user_choice =  input(" Enter your choice (snake,water,gun) : ").lower()

if user_choice not in choices:
    print (" Invalid choice you have selected . Please choose snake, water or gun .")
else:
    computer_choice = random.choice(choices) 
    print(f" Computer chose: {computer_choice}")
    result = game_result(user_choice , computer_choice)
    print(result)           
         