from turtle import Turtle
import random

PURPLE = "#6807F9"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color(PURPLE)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def reset_ball(self):
        self.setposition(0, 0)
        self.x_bounce()
        self.ball_speed = .1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def x_bounce(self):
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1

    def speed_up(self):
        if self.ball_speed > .01:
            self.ball_speed -= .01
        else:
            self.ball_speed -= .001

