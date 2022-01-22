# object oriented programming
import another_module

print(another_module.another_variable)

# import turtle
#
# # creating turtle object called timmy
# timmy = turtle.Turtle()

from turtle import Turtle, Screen
# creating turtle object called timmy
timmy = Turtle()
print(timmy)
# changed the pen to turtle shape
timmy.shape("turtle")
# changed the turtle color to red
timmy.color("red")

my_screen = Screen()
print(my_screen.canvheight)

# Object Methods
my_screen.exitonclick()