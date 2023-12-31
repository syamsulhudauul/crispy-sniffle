student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    #Access value.student or value.score
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
file_data =  pandas.read_csv("./nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index,row) in file_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = ""
def generate_phonetic(): 
    try:
        global user_input
        user_input = input("Enter a word: ").upper()
    except not user_input.isalpha():
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print("Another error")

result = [nato_dict[letter] for letter in user_input]
print(result)


