from turtle import Turtle

snake_width = 1
snake_length = 1
snake_outline = 1

moving_distance = 20
segment_distance = 20

x = 0 
y = 0 

class Snake :

    def __init__(self):
        self.r = 255
        self.g = 0
        self.b = 0
        self.snake_segments = []
        self.game_boundary()
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def game_boundary(self):
        tim = Turtle()
        tim.hideturtle()
        tim.color("black")
        tim.pensize(7.5)
        tim.speed(0)
        tim.penup()
        tim.setpos(-315 , -315)
        tim.pendown()
        tim.fillcolor("white")
        tim.begin_fill()

        for i in range(4):
            tim.forward(630)
            tim.left(90)

        tim.end_fill()

    def snake_body(self,x,y):
        snake = Turtle(shape="square")
        snake.shapesize(snake_width , snake_length , snake_outline)
        snake.color(self.r , self.g , self.b)
        snake.speed(0)
        snake.penup()
        snake.setpos(x,y)
        self.snake_segments.append(snake)
        x -= segment_distance

    def create_snake(self):
        for i in range(3):
            self.snake_body(x,y)
            
    def move_snake(self):

        for i in range(len(self.snake_segments)-1 , 0 ,-1):
            snake_x = self.snake_segments[i-1].xcor()
            snake_y = self.snake_segments[i-1].ycor()


            self.snake_segments[i].setpos(snake_x,snake_y)

        self.snake_head.forward(moving_distance)


    def snake_length(self):
        self.snake_body(self.snake_segments[-1].xcor(), self.snake_segments[-1].ycor())


    def move_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.seth(0)
        
    def move_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.seth(180)
        
    def move_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.seth(90)
        
    def move_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.seth(270)


    def snake_color(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b


