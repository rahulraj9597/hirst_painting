from random import random
from turtle import Turtle,Screen
import random
import time

my_screen = Screen()

colors = ['red','blue','violet','green','yellow','black','pink','orange']
my_screen.tracer(0)
spot_paint = Turtle()
spot_paint.penup()
spot_paint.goto(-200,-200)
spot_paint.pendown()
spot_paint.hideturtle()

while True:
    spot_paint.penup()
    spot_paint.goto(-200,-200)
    for i in range(0,6):
        for i in range(1,9):
            spot_paint.penup()
            spot_paint.dot(50,random.choice(colors))
            spot_paint.forward(100)
            spot_paint.pendown()
        spot_paint.setheading(90)
        spot_paint.penup()
        spot_paint.forward(100)
        spot_paint.setheading(180)
        spot_paint.forward(800)
        spot_paint.setheading(0)
        spot_paint.pendown()
    time.sleep(1)
    my_screen.update()


my_screen.exitonclick()