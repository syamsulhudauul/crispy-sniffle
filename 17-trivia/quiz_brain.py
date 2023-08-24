#Create a class called QuizBrain
class QuizBrain:
    # write an __init__() method
    def __init__(self,question_list):
        # initialise the question_number to 0
        self.question_number = 0
        # initialise the question_list to an input
        self.question_list = question_list
        self.score = 0

    # write a method called next_question()
    def next_question(self):
        # create a variable called current_question and set it to the current question number from the question_list
        current_question = self.question_list[self.question_number]
        # create a variable called user_answer and set it to the input from the user
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # increment the question_number by 1
        self.question_number += 1
        # create a variable called check_answer and set it to the check_answer method
        self.check_answer(user_answer,current_question.answer)
    
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    



