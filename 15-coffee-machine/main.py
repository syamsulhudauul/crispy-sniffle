import os 
import time 

def clear():
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    # TODO: 1 Print report from all of the resources
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")

def check_resources(opt):
    # check option is available in the menu
    if opt not in MENU:
        print("Please input correct option!!!")
        return False
    return True

def check_sufficient(opt):
    check_water = resources['water'] - MENU[opt]['ingredients']['water']
    check_milk = resources['milk'] - MENU[opt]['ingredients']['milk']
    check_coffee = resources['coffee'] - MENU[opt]['ingredients']['coffee']

    if check_water < 0:
        print("Sorry there is not enough water.")
        return False 
    elif check_milk < 0:
        print("Sorry there is not enough milk.")
        return False
    elif check_coffee < 0:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    money = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return money

def check_money(money,opt):
    if money < MENU[opt]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money >= MENU[opt]['cost']:
        change = money - MENU[opt]['cost']
        print(f"Here is ${change} in change.")
        return True

def update_resource(opt):
    check_water = resources['water'] - MENU[opt]['ingredients']['water']
    check_milk = resources['milk'] - MENU[opt]['ingredients']['milk']
    check_coffee = resources['coffee'] - MENU[opt]['ingredients']['coffee']
    resources['water'] = check_water- MENU[opt]['ingredients']['water']
    resources['milk'] = check_milk - MENU[opt]['ingredients']['milk']
    resources['coffee'] = check_coffee - MENU[opt]['ingredients']['coffee']
    return resources

while True:
    clear()
    opt=input("What would you like? (espresso/latte/cappuccino):")
    if opt == "report":
        report()
        time.sleep(1)
        continue
    else:
        # check option is available in the menu
        if check_resources(opt) == False:
            time.sleep(1)
            continue

        # TODO: 2 Check resources sufficient?
        if not check_sufficient(opt):
            time.sleep(1)
            continue
        
        # TODO: 3 Process coins
        print(f"You chose {opt} with cost ${MENU[opt]['cost']}")
        money = process_coins()
        if not check_money(money,opt):
            print("Sorry that's not enough money. Money refunded.")
            time.sleep(5)
            continue
        else:
            resources = update_resource(opt)
            print("The coffee is ready!!!")
            time.sleep(5)
            continue 


