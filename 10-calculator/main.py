#Calculator
from art import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(a,b):
  return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_calculation == "n":
            should_continue = False
            clear()
            calculator()
        elif continue_calculation == "y":
            num1 = answer
        else:
            print("Invalid input")
            break

calculator()
