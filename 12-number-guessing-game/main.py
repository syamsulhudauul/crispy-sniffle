#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random



def input_number():
    innum = ""
    while innum == "":
        innum = input("Make a guess: ")
        if innum == "":
            print("Please input your number!!!")
        else:
            return innum

def check_number(answer,guess,turns):
    if answer == guess :
        print(f"You got it! The answer was {answer}")
        return -1
    elif answer > guess:
        print("Too low")
        return turns-1
    else:
        print("Too high")
        return turns-1

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1,100)
    guess = -1
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        turns = 10
    else:
        turns = 5

    while guess != answer:
        print(f"You have {turns} remaining to guess the number")

        # innum = input("Make a guess: ")
        guess = int(input_number())
        # i = int(innum)
        turns = check_number(answer,guess,turns) 
        if turns == 0:
            print(f"You lose. The answer was {answer}")
            return

game()