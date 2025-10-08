# Toheeb Guessin Game
import random
#Function to set difficulty level
def set_difficulty():
    while True:
        level=input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
        if level=="easy":
           return 10
        elif level=='hard':
           return 5
        else:
             print("Invalid choice. Please type 'easy' or 'hard'.")
# Function to check user Guess and give feedback
def check_guess(guess,answer,attempts):
    if guess==answer:
        print(f"Congratulations the answer was {answer}.\n")
        return 0
    elif abs(guess-answer)<=3:
        print(" ohh You are very close!")
    elif guess>answer:
        print("Too high")
    else:
        print("Too low")
    return attempts -1
# Main game logic
def play_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer=random.randint(1,100)
    attempts=set_difficulty()
    
    guess=None
    while attempts > 0 and guess !=answer:
        print(f"\nYou have {attempts} attempts remaining.")
        try:
            guess=int(input("Make a guess :"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts=check_guess(guess,answer,attempts)
        if attempts ==0 and guess != answer:
            print(f"Sorry You run out of guess the correct number was {answer}.\n")
        elif guess != answer and attempts >0:
            print("Guess again...")
# Game loop for replay
def start_game():
    while True:
        play_game()
        again=input("Do you want to play again ?Type 'yes' or 'no':").lower()
        if again !='yes':
            print("Thanks for playing! Goodbye.")
            break
        

start_game()
