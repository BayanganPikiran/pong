from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.speed('fastest')
