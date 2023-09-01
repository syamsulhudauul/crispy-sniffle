from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",24, "normal")
FILE_PATH = "./data.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open(FILE_PATH) as data:
            self.high_score = int(data.read())
            data.close()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_PATH,mode="w") as data:
                data.write(str(self.high_score))
                data.close()
        self.score = 0
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        # self.clear() #keep see the score
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

