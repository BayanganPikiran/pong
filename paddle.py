from turtle import Turtle

MOVE_DISTANCE = 10

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.speed('fastest')

    def paddle_up(self):
        self.forward(MOVE_DISTANCE)

    def paddle_down(self):
        self.backward(MOVE_DISTANCE)

    # def paddle2_up(self):
    #     self.forward(MOVE_DISTANCE)
    #
    # def paddle2_down(self):
    #     self.backward(MOVE_DISTANCE)

