from turtle import Turtle
import random

food_width = 0.5
food_length = 0.5
food_outline = 0.5


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.rvalue = 0
        self.gvalue = 0
        self.bvalue = 0

        self.shape("circle")
        self.shapesize(food_width,food_length,food_outline)
        self.speed(0)
        self.penup()
        self.snake_food()

    def snake_food(self):
        food_x = random.randint(-300, 300)
        food_y = random.randint(-300, 300)
        self.food_color()
        self.setpos(food_x, food_y)

    def food_color(self):
        r = random.randint(0, 200)
        g = random.randint(0, 200)
        b = random.randint(0, 200)

        self.rvalue = r
        self.gvalue = g
        self.bvalue = b

        self.color((r,g,b))

        
