#5-password-generator

#Password Generator Project
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for letter in range(0, nr_letters):
    password += random.choice(alfabet)
for symbol in range(0, nr_symbols):
    password += random.choice(symbols)
for number in range(0, nr_numbers):
    password += random.choice(numbers)
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for letter in range(0, nr_letters):
    password_list.append(random.choice(alfabet))
for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)
