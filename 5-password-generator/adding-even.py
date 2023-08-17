#adding-even.py
# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 2 and 100.
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
# Hint
# There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.
# Solution
# https://repl.it/@appbrewery/day-5-2-solution
# Write your code below this row 👇
total = 0
for number in range(2, 101, 2):
    total += number
print(total)
#or
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)