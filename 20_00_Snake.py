from turtle import Turtle, Screen
import time

MOVEDISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("green")
    
    def create_snake(self):
        for position in starting_position:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    def move(self):
        #for seg_num in range(start,stop,step):
        for seg_num in range(len(self.segments)-1,0,-1):
            #for loop has no impact on the first segment=self.head
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVEDISTANCE)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

screen= Screen()
screen.setup(width=600, height=600)
#screen segment is 20x20
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #turn off the screen updates

starting_position = [(0,0), (-20,0), (-40,0)]
snake= Snake()

screen.listen() #listen for key presses
screen.onkey(snake.up, "Up") #when the up arrow is pressed, call the up method of the snake object
screen.onkey(snake.down, "Down") #when the down arrow is pressed, call the down method of the snake object  
screen.onkey(snake.left, "Left") #when the left arrow is pressed, call the left method of the snake object
screen.onkey(snake.right, "Right") #when the right arrow is pressed, call the right method of the snake object


game_is_on = True
while game_is_on:
    screen.update() #update the screen to show the segments
    time.sleep(0.25) #pause for a short time to control the speed of the game

    snake.move()
screen.exitonclick()