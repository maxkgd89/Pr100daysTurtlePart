import random as rd
from turtle import Screen, Turtle

tim = Turtle()
screen=Screen()
colors=["red","blue","green","yellow","purple","orange","pink","brown","black","white"]

num_sides = 5
def draw_shape(num_sides):
  angle = 360/num_sides
  for _ in range(num_sides):
    tim.forward(20)
    tim.right(angle)

for i in range(3,11):
  tim.color(rd.choice(colors))
  draw_shape(num_sides)
  num_sides += i



screen.exitonclick()