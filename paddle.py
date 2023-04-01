from turtle import Turtle

MOVE_DISTANCE = 10

class Paddle(Turtle):

    def __init__(self, coordinates, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.goto(coordinates)
        self.color(color)

    def paddle_up(self):
        if self.ycor() < 191:
            self.forward(MOVE_DISTANCE)

    def paddle_down(self):
        if self.ycor() > -191:
            self.backward(MOVE_DISTANCE)


