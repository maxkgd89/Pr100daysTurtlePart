
from prettytable import PrettyTable
from turtle import Turtle, Screen

# Create table for turtle stats
table = PrettyTable()
table.field_names = ["Name", "Color", "Speed"]
table.add_row(["Timmy", "coral", "normal"])
print("\nTurtle Stats:")
print(table)

# Original turtle code
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()
