# PROJECT ON SNAKE GAME

from turtle import Screen , Turtle
import random
import time
from snake import Snake
from food import Food
from score import Score
from boundary import Boundary

myscreen = Screen()
myscreen.setup(1350,1000,0,0)
myscreen.title("SNAKE GAME")
myscreen.colormode(255)
myscreen.bgcolor("grey")

myscreen.tracer(0)

boundary = Boundary()
snake = Snake()
food = Food()
score = Score()
logo = Score()

score.scoreboard()
logo.game_logo()

myscreen.update()

level = myscreen.textinput("DIFFICULTY LEVEL", "Choose difficulty level : Easy , Medium , Hard ?")

time.sleep(0.5)

myscreen.listen()

myscreen.onkey(snake.move_up, "Up")
myscreen.onkey(snake.move_down, "Down")
myscreen.onkey(snake.move_left, "Left")
myscreen.onkey(snake.move_right, "Right")

difficulty = {
    "EASY" : 0.20,
    "MEDIUM" : 0.15,
    "HARD" : 0.10
}

if level:
    end = False
else:
    end = True

sleep_time = difficulty.get(level.upper())

while not end:
    myscreen.update()
    time.sleep(sleep_time)
    snake.move_snake()

    r = food.rvalue
    g = food.gvalue
    b = food.bvalue

    snake.snake_color(r, g, b)

    if snake.snake_head.distance(food) <= 15:
        snake.snake_length()
        score.scoreboard()
        food.snake_food()

    if snake.snake_head.xcor() <= -315 or snake.snake_head.xcor() >= 315 or snake.snake_head.ycor() <= -315 or snake.snake_head.ycor() >= 315:
        score.game_over()
        end = True

    for segments in snake.snake_segments[1:]:
        if snake.snake_head.distance(segments) <= 10:
            score.game_over()
            end = True

myscreen.exitonclick()


