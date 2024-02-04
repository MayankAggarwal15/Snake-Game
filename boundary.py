from turtle import Turtle


class Boundary :

    def __init__(self):
        self.game_boundary()

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
