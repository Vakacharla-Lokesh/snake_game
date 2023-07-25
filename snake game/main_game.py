from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_scoreboard = ScoreBoard()


my_screen.listen()


game_stat = True

while game_stat:
    my_screen.update()
    time.sleep(0.2)
    my_screen.onkeypress(my_snake.up, "Up")
    my_screen.onkeypress(my_snake.down, "Down")
    my_screen.onkeypress(my_snake.left, "Left")
    my_screen.onkeypress(my_snake.right, "Right")
    my_snake.move()

    #detecting colission with food
    if my_snake.head.distance(my_food) < 15:
        my_food.new_food()
        my_snake.extend()
        my_scoreboard.point_scored()
    #detecting collission with walls
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        my_scoreboard.reset_game()
        my_snake.reset_snake()

    #detect collission with tail
    for seg in my_snake.segments[3:]:
        if my_snake.head.distance(seg) < 10:
            my_scoreboard.reset_game()
            my_snake.reset_snake()

my_screen.exitonclick()