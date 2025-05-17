from turtle import Screen, color
import turtle as t
import random

tim=t.Turtle()
screen=Screen()
tim.speed("fastest")

for _ in range(100):

  tim.circle(100)
  current_heading=tim.heading()
  tim.setheading(current_heading+10)


t.colormode(255)
def random_color():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  color2=(r,g,b)
  return color2

screen.exitonclick()