from turtle import Turtle, Screen

screen= Screen()
screen.setup(width=600, height=600)
#screen segment is 20x20
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0,0), (-20,0), (-40,0)]

segments = []

#create, color, and position the segments
for position in starting_position:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

#move the segments
game_is_on = True
while game_is_on:
    for seg in segments:
        seg.backward(20)

screen.exitonclick()