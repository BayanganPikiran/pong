from turtle import Screen
from paddle import Paddle

SCREEN_AZURE = "#F0FFFF"
PADDLE1_GREEN = "#06FF00"
PADDLE2_RED = "#FF1700"

screen = Screen()
screen.bgcolor(SCREEN_AZURE)
screen.setup(width=800)
screen.title("Ping-Pong Ding-Dong")

paddle1 = Paddle()
paddle1.color(PADDLE1_GREEN)
paddle1.color()
paddle2 = Paddle()
paddle2.color(PADDLE2_RED)

paddle1.goto(-375, 0)
paddle2.goto(375, 0)



screen.exitonclick()

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
