from turtle import Turtle
import random

PURPLE = "#6807F9"
PADDLE_DISTANCE = 13


class Ball(Turtle):

    def __init__(self, paddle1, paddle2):
        super().__init__()
        self.paddle1 = paddle1
        self.paddle2 = paddle2
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

    def detect_wall_collision(self):
        if self.ycor() < -238:
            self.setheading(360 - self.heading())
        elif self.ycor() > 238:
            self.setheading(360 - self.heading())

    def detect_paddle_collision(self):
        if self.distance(self.paddle1) < PADDLE_DISTANCE and self.heading() < 180:
            self.setheading(self.heading() + 180)
        elif self.distance(self.paddle1) < PADDLE_DISTANCE and self.heading() > 180:
            self.setheading(self.heading() - 180)
        elif self.distance(self.paddle2) < PADDLE_DISTANCE and self.heading() < 90:
            self.setheading(self.heading() + 180)
        elif self.distance(self.paddle2) < PADDLE_DISTANCE and self.heading() > 90:
            self.setheading(self.heading() - 180)

    def ball_move(self):
        self.forward(10)
        self.detect_wall_collision()
        self.detect_paddle_collision()







