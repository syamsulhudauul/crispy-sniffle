# project 4: rock paper scissors
#
# type rock paper scissors ASCII art
def print_choice(choice):
    if choice == 0:
        print('''
            _______
        ---'   ____)
                (_____)
                (_____)
                (____)
        ---.__(___)
        ''')
    elif choice == 1:
        print('''
            _______
        ---'   ____)____
                    ______)
                    _______)
                    _______)
        ---.__________)
        ''')
    elif choice == 2:
        print('''
            _______
        ---'   ____)____
                    ______)
                __________) 
                (____)  
        ---.__(___) 
        ''')
      
      
# import random module
import random

# create a list of rock, paper, scissors
rps = ["rock", "paper", "scissors"]

# create a variable to store the user's choice
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")


# create a variable to store the computer's choice
computer_choice = random.randint(0, 2)

# print the user's choice
print(f"You chose {rps[int(user_choice)]}.")
print_choice(int(user_choice))
# print the computer's choice
print(f"The computer chose {rps[computer_choice]}.")
print_choice(computer_choice)

# print the result
if int(user_choice) >= 3 or int(user_choice) < 0:
    print("You typed an invalid number, you lose!")
elif int(user_choice) == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and int(user_choice) == 2:
    print("You lose!")
elif computer_choice > int(user_choice):
    print("You lose!")
elif int(user_choice) > computer_choice:
    print("You win!")
elif computer_choice == int(user_choice):
    print("It's a draw!")

# compare this to the solution:
# https://repl.it/@appbrewery/rock-paper-scissors-start
# https://repl.it/@appbrewery/rock-paper-scissors-final
