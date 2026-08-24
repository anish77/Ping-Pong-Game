from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.drow_the_line()

    def drow_the_line(self):
        for y in range(-300, 300, 20):
            self.goto(0, y)
            self.pendown()
            self.goto(0, y + 10)
            self.penup()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Curier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Curier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        self.drow_the_line()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        self.drow_the_line()