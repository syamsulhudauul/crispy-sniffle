print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total = bill * (1 + tip / 100)
total_per_person = total / people
print(f"Each person should pay: ${total_per_person:.2f}")