#student grades
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_graders = {}


for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_graders[student] = "Outstanding"
    elif score > 80:
        student_graders[student] = "Exceeds Expectations"
    elif score > 70:
        student_graders[student] = "Acceptable"
    else:
        student_graders[student] = "Fail"

print(student_graders)