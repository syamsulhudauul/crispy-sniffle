f = open("./input/Letters/starting_letter.txt")
f2 = open("./input/Names/invited_names.txt")
users = f2.readlines()
letter = f.read()
f.close()
f2.close()

for user in users:
    user = user.strip()
    new_letter = letter.replace("[name]",user)
    new_file = open(f"./output/ReadyToSend/letter_for_{user}.txt",mode="w")
    new_file.write(new_letter)
    new_file.close()