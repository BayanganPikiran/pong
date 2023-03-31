import time
from turtle import Screen
from paddle import Paddle
from ball import Ball



SCREEN_AZURE = "#F0FFFF"
GREEN = "#06FF00"
RED = "#FF1700"

PADDLE1_COORDINATES = (-375, 0)
PADDLE2_COORDINATES = (375, 0)

screen = Screen()
screen.bgcolor(SCREEN_AZURE)
screen.setup(width=800, height=506)
screen.title("Ping-Pong Ding-Dong")
screen.listen()
screen.tracer(0)


left_paddle = Paddle(PADDLE1_COORDINATES, GREEN)
right_paddle = Paddle(PADDLE2_COORDINATES, RED)

screen.onkeypress(left_paddle.paddle_up, "w")
screen.onkeypress(left_paddle.paddle_down, "x")
screen.onkeypress(right_paddle.paddle_up, "Up")
screen.onkeypress(right_paddle.paddle_down, "Down")

# left_paddle.place_paddle(PADDLE1_COORDINATES)
# right_paddle.place_paddle(PADDLE2_COORDINATES)

ball = Ball()



# def sleep():
#     sleep_rate = 0.1
#     time.sleep(sleep_rate)
#     if ball.detect_paddle_collision():
#         if sleep_rate > .01:
#             sleep_rate -= .01
#         elif sleep_rate < .01:
#             sleep_rate -= .001


game_is_on = True
while game_is_on:
    ball.ball_start()
    if ball.heading() == 0 or ball.heading() == 180:
        ball.ball_start()
    else:
        match_in_play = True
        while match_in_play:
            time.sleep(.1)
            screen.update()
            ball.move()
            if ball.ycor() < -238 or ball.ycor() > 238:
                ball.y_bounce()
            if ball.distance(left_paddle) < 50 and ball.xcor() < -355:
                ball.x_bounce()
            if ball.distance(right_paddle) < 50 and ball.xcor() > 355:
                ball.x_bounce()




screen.exitonclick()

# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
