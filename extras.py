from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
bob = Turtle()
bob.shape("circle")
bob.color("red")
bob.speed(1)

#Challenge to make a dashed line
def dashed_line(turtle, length, dash_length, space):
    while length >= 0:
        turtle.penup()
        turtle.forward(dash_length)
        turtle.pendown()
        turtle.forward(space)
        turtle.penup()
        length -= (dash_length + space)

#Challenge to make any shape
def shape_creation(turtle, sides, length):
    total_length = length * sides
    while total_length != 0:
        turtle.forward(length)
        turtle.right(360/sides)
        total_length -= length

#Challenge to make a random walk function
def random_walk(turtle, length_per_walk, thickness, walks, speed):
    turtle.speed(speed)
    while walks != 0:
        turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.right(90 * random.randint(0, 4))
        turtle.forward(length_per_walk)
        turtle.pen(pensize=thickness)
        walks -= 1

#Challenge to make a spirograph maker
def spirograph(turtle, radius, number_of_circles, speed):
    circles = number_of_circles
    turtle.speed(speed)
    while circles != 0:
        turtle.circle(radius)
        turtle.rt(360/number_of_circles)
        circles -= 1



screen.exitonclick()



