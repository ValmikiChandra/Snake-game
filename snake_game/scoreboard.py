from turtle import Turtle

ALIGNMENT="center"
FONT=("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt", mode="r") as data:
            self.high_score=int(data.read())
        self.penup()
        self.color("white")
        self.goto(x=0, y=260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()


    def increase_score(self):
        self.score+=1
        self.speed("fastest")
        self.update_score()



