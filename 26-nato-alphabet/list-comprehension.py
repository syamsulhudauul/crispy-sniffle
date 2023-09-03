list = [1,2,3,4,5,6,7,8,9,10]
new_list = [2**n for n in list]
print(new_list)

#even numbers -> with condition
even_list = [n for n in list if n % 2 == 0]
print(even_list)

temp = [n for n in range(1,5)]
print(temp)
new_l = [n**(1/2) for n in temp]
print(new_l)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_names = [name.upper() for name in names if len(name) > 5]
print(new_names)

# Data overlap
# result = [int(num) for num in file1_data if num in file2_data]
# output -> [3, 6, 5, 33, 12, 7, 42, 13]

# Dictionary Comprehension
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name:random.randint(1,100) for name in names}
print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score > 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

# Dictionary Comprehension with condition
weather_c = {
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24
}

weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)