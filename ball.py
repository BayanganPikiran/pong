from turtle import Turtle

PURPLE = "#6807F9"
HEADING = [0, 90, 180, 270]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.color(PURPLE)
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.goto(0, 0)
        self.showturtle()