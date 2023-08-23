# import packages
from art import logo, vs
from game_data import data
import random
import os

def clear():
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

# load dataset
data = data

def get_random_data():
    # get random data
    data1 = random.choice(data)
    data2 = random.choice(data)
    if data1 == data2:
        data2 = random.choice(data)
    return data1, data2

def get_next_random(data1):
    data2 = random.choice(data)
    if data1 == data2:
        data2 = random.choice(data)
    return data2

def get_answer(data1,data2):
    if data1['follower_count'] > data2['follower_count']:
        return 'A'
    else:
        return 'B'

def game():
    print(logo)
    score = 0
    is_failed = False
    data1 = random.choice(data)
    while not is_failed:
        #get random data
        data2 = get_next_random(data1)
        print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}")
        print(vs)
        print(f"Against B: {data2['name']}, a {data2['description']}, from {data2['country']}")
        option=input("Who has more followers? Type 'A' or 'B':")
        answer=get_answer(data1,data2)

        #clear screen
        clear()
        print(logo)
        if option.lower() == answer.lower():
            score +=1
            data1 = data2
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return 
        
game()