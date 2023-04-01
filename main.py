import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()
ball = Ball()

screen.onkeypress(left_paddle.paddle_up, "w")
screen.onkeypress(left_paddle.paddle_down, "x")
screen.onkeypress(right_paddle.paddle_up, "Up")
screen.onkeypress(right_paddle.paddle_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() < -238 or ball.ycor() > 238:
        ball.y_bounce()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -355 or\
            ball.distance(right_paddle) < 50 and ball.xcor() > 355:
        ball.x_bounce()
        ball.speed_up()
    if ball.xcor() < - 365:
        scoreboard.update_r_score()
        scoreboard.write_score()
        ball.reset_ball()
    if ball.xcor() > 365:
        scoreboard.update_l_score()
        scoreboard.write_score()
        ball.reset_ball()
    if scoreboard.l_score == 5:
        play_on = screen.textinput("Restart", "Player 1 wins.\nDo you want to play again? Type 'y' or 'n'.")
        if play_on == 'y':
            screen.listen()
            scoreboard.clear()
            scoreboard = Scoreboard()
            ball.move()
        else:
            game_is_on = False
            scoreboard.write_game_over()
    if scoreboard.r_score == 5:
        play_on = screen.textinput("Restart", "Player 2 wins.\nDo you want to play again? Type 'y' or 'n'.")
        if play_on == 'y':
            screen.listen()
            scoreboard.clear()
            scoreboard = Scoreboard()
            ball.move()
        else:
            game_is_on = False
            scoreboard.write_game_over()











screen.exitonclick()

# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
