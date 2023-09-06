# FileNotFoundError
try:
    f = open('test.txt')
    print(f.read())
    f.close()
except FileNotFoundError:
    f = open('test.txt', 'w')
    f.write('Something')
    f.close()
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
finally:
    f = open('test.txt')
    print(f.read())
    f.close()

# KeyError
a_dictionary = {"key": "value"}
try:
    value = a_dictionary["non_existent_key"]
except KeyError:
    print("That key doesn't exist!")

# IndexError
try:
    fruit_list = ["Apple", "Banana", "Pear"]
    fruit = fruit_list[3]
except IndexError:
    print("That index doesn't exist!")

# ValueError
try:
    text = "abc"
    number = int(text)
except ValueError:
    print(f"The text {text} is not a number.")

# TypeError
try:
    text = "abc"
    print(5 + text)
except TypeError:
    print("Something is wrong with the types!")

# NameError
try:
    print(non_existent_variable)
except NameError:
    print("That variable doesn't exist!")
    
# AttributeError
try:
    print("abc".append("d"))
except AttributeError:
    print("Strings don't have an append() method")

# ZeroDivisionError
try: 
    10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# ImportError
try:
    from math import squareroot
except ImportError:
    print("Import failed!")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

if weight < 45 or weight > 150:
    raise ValueError("Human weight should not be less than 45 kg or over 150 kg.")

bmi = weight / height ** 2


