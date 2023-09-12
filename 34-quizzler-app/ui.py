from  tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizz_brain):
        self.quiz = quizz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0,column=1)

        #text canvas 
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1,column=0,columnspan=2)
        self.question_text=self.canvas.create_text(150,125,width=280,text='Some Question Text',font=("Arial",20,"italic"),fill=THEME_COLOR)

        check_image = PhotoImage(file="images/true.png",)
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.check)
        self.check_button.grid(row=2, column=0)

        cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.cross)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the question")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def check(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def cross(self):
        is_right = self.quiz.check_answer("False") 
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        



