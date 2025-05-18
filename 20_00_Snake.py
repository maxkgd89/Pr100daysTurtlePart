from turtle import Turtle, Screen
import time

screen= Screen()
screen.setup(width=600, height=600)
#screen segment is 20x20
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #turn off the screen updates

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
    screen.update() #update the screen to show the segments
    for seg in segments:
        seg.forward(20)
        time.sleep(0.25) #pause for a short time to control the speed of the game
    segments[0].left(90) #move the first segment left


screen.exitonclick()