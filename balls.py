from turtle import Turtle
import random

PURPLE = "#6807F9"
PADDLE_DISTANCE_SHORT = 13
PADDLE_DISTANCE_LONG = 50


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
        if self.ycor() < -238 or self.ycor() > 238:
            self.setheading(360 - self.heading())

    def down_180(self):
        self.setheading(self.heading() - 180)

    def up_180(self):
        self.setheading(self.heading() + 180)

    def less_than_paddle_short(self, paddle):
        """used for collisions in center of paddle, i.e. 45 to 135-degree angle"""
        return self.distance(paddle) < PADDLE_DISTANCE_SHORT

    def less_than_paddle_long(self, paddle):
        """used for collisions on edges of paddle, i.e. 45-degree > or > 135-degree"""
        if paddle == self.paddle1:
            return self.xcor() < -365 and self.distance(paddle) < PADDLE_DISTANCE_LONG
        elif paddle == self.paddle2:
            return self.xcor() > 365 and self.distance(paddle) < PADDLE_DISTANCE_LONG

    def detect_paddle1_collision(self):
        if self.less_than_paddle_short(self.paddle1) and self.heading() < 180:
            self.up_180()
        elif self.less_than_paddle_long(self.paddle1) and self.heading() < 180:
            self.up_180()
        elif self.less_than_paddle_short(self.paddle1) and self.heading() > 180:
            self.down_180()
        elif self.less_than_paddle_long(self.paddle1) and self.heading() > 180:
            self.down_180()

    def detect_paddle2_collision(self):
        if self.less_than_paddle_short(self.paddle2) and self.heading() < 90:
            self.up_180()
        elif self.less_than_paddle_long(self.paddle2) and self.heading() < 90:
            self.up_180()
        elif self.less_than_paddle_short(self.paddle2) and self.heading() > 90:
            self.down_180()
        elif self.less_than_paddle_long(self.paddle2) and self.heading() > 90:
            self.down_180()

    # def detect_paddle_collision(self):
    #     if self.distance(self.paddle1) < PADDLE_DISTANCE_SHORT and self.heading() < 180:
    #         self.setheading(self.heading() + 180)
    #     elif self.distance(self.paddle1) < PADDLE_DISTANCE_SHORT and self.heading() > 180:
    #         self.setheading(self.heading() - 180)
    #     elif self.distance(self.paddle2) < PADDLE_DISTANCE_SHORT and self.heading() < 90:
    #         self.setheading(self.heading() + 180)
    #     elif self.distance(self.paddle2) < PADDLE_DISTANCE_SHORT and self.heading() > 90:
    #         self.setheading(self.heading() - 180)

    def ball_move(self):
        self.forward(10)
        self.detect_wall_collision()
        self.detect_paddle1_collision()
        self.detect_paddle2_collision()
        # self.detect_paddle_collision()







