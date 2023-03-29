from turtle import Turtle
import random

PURPLE = "#6807F9"


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("circle")
        self.penup()
        self.color(PURPLE)
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        # self.goto(0, 0)
        # self.showturtle()

    def ball_start(self):
        self.setposition (0, 0)
        ball_heading = random.randint(1, 360)
        self.setheading(ball_heading)

    def ball_move(self):
        self.forward(10)
        if self.ycor() < -238:
            self.setheading(360 - self.heading())
        elif self.ycor() > 238:
            self.setheading(360 - self.heading())





