from turtle import Turtle


ORANGE = "#FF8B13"
FONT = ("Courier", 30, "bold")
SMALL_FONT = ("Courier", 16, "bold")

P1 = (-200, 210)
P1_SCORE_POSITION = (-200, 160)
P2 = (200, 210)
P2_SCORE_POSITION = (200, 160)
CENTER_POSITION = (0, 0)

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

    def reset_score(self):
        self.score = [0, 0]


    def update_r_score(self):
        self.r_score += 1

    def update_l_score(self):
        self.l_score += 1

    def write_score(self):
        self.clear()
        self.goto(P1)
        self.write("Player 1", align="center", font=SMALL_FONT)
        self.goto(P2)
        self.write("Player 2", align="center", font=SMALL_FONT)
        self.goto(P1_SCORE_POSITION)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(P2_SCORE_POSITION)
        self.write(self.r_score, align="center", font=FONT)

    def write_game_over(self):
        self.goto(CENTER_POSITION)
        self.write("Your paddle skills are weak!\n  Go play with your balls!", align="center", font=FONT)





