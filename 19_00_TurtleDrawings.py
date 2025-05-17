from turtle import Turtle, Screen

tim= Turtle()
screan= Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()




screan.listen()
#screan.onkey(key="space", fun=move_forwards)
screan.onkey(move_forwards,"w")
screan.onkey(move_backwards, "s")
screan.onkey(turn_left, "a")
screan.onkey(turn_right, "d")
screan.onkey(clear, "c")
screan.exitonclick()