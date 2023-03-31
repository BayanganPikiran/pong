from turtle import Turtle


ORANGE = "#FF8B13"
FONT = ("Courier", 30, "bold")

LEFT_SCORE_POSITION = (-100, 180)
RIGHT_SCORE_POSITION = (100, 180)
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.l_score = self.score[0]
        self.r_score = self.score[1]
        self.color(ORANGE)
        self.hideturtle()
        self.penup()
        self.write_score()

    def update_r_score(self):
        self.r_score += 1

    def update_l_score(self):
        self.l_score += 1

    def write_score(self):
        self.clear()
        self.goto(LEFT_SCORE_POSITION)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(RIGHT_SCORE_POSITION)
        self.write(self.r_score, align="center", font=FONT)

