from turtle import Turtle, Screen

import random

tim = Turtle()
screen = Screen()

import turtle
turtle.colormode(255)

rgb_colors = []
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)


for color in colors:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_colors.append((r, g, b))
    #I made 6 random RGB colors


tim.speed("fastest")

for _ in range(10):
    tim.dot(20, random.choice(rgb_colors))
    tim.penup
    tim.forward(50)
    tim.penup
screen.exitonclick()