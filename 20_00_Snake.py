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
    time.sleep(0.25) #pause for a short time to control the speed of the game
    #for seg_num in range(start,stop,step):
    for seg_num in range(len(segments)-1,0,-1):
        new_x=segments[seg_num-1].xcor()
        new_y=segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20) #move the first segment forward
    segments[0].left(90) #move the first segment forward
screen.exitonclick()