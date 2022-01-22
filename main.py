# # object oriented programming
# import another_module
#
# print(another_module.another_variable)
# refer https://docs.python.org/3/library/turtle.html for turtle documentation
# # import turtle
# #
# # # creating turtle object called timmy
# # timmy = turtle.Turtle()
#
# from turtle import Turtle, Screen
# # creating turtle object called timmy
# timmy = Turtle()
# print(timmy)
# # changed the pen to turtle shape
# timmy.shape("turtle")
# # changed the turtle color to red
# timmy.color("red")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# # Object Methods
# my_screen.exitonclick()

# refer https://pypi.org/project/prettytable/ for PrettyTable documentation
from prettytable import PrettyTable
table = PrettyTable()
#print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# aligning the table to the left
table.align = "l"
print(table)

# object attributes
