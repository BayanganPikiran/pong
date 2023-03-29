import time
from turtle import Screen
from paddle import Paddle
from ball import Ball


SCREEN_AZURE = "#F0FFFF"
PADDLE1_GREEN = "#06FF00"
PADDLE2_RED = "#FF1700"

PADDLE1_COORDINATES = (-375, 0)
PADDLE2_COORDINATES = (375, 0)

screen = Screen()
screen.bgcolor(SCREEN_AZURE)
screen.setup(width=800)
screen.title("Ping-Pong Ding-Dong")
screen.listen()
screen.tracer(0)


paddle1 = Paddle()
paddle1.color(PADDLE1_GREEN)
paddle2 = Paddle()
paddle2.color(PADDLE2_RED)

screen.onkeypress(paddle1.paddle_up, "w")
screen.onkeypress(paddle1.paddle_down, "x")
screen.onkeypress(paddle2.paddle_up, "Up")
screen.onkeypress(paddle2.paddle_down, "Down")

paddle1.place_paddle(PADDLE1_COORDINATES)
paddle2.place_paddle(PADDLE2_COORDINATES)

ball = Ball()
ball.ball_start()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.ball_move()



screen.exitonclick()

# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
