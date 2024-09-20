import colorgram
from turtle import Turtle, Screen
import random
#Make sure to download the colorgram package to make this work!

#Gathers colors from an image
rgb_stuff = []
colors = colorgram.extract('imageimage.jpg', 25)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_stuff.append(new_color)

#Variable Setup
bob = Turtle()
bob.speed(1000)
screen = Screen()
screen.colormode(255)


#The Hirst Dot Process.
def hirst_dots(turtle, rows, columns, length, height, radius):


    x = -0.5*length
    y = -0.5*height

    turtle.teleport(x, y)
    num_len = length
    num_hei = height

    while num_hei != 0:
        num_len = length

        while num_len != 0:

            color_chosen = random.choice(rgb_stuff)
            turtle.color(color_chosen)
            turtle.begin_fill()
            turtle.circle(radius)
            turtle.end_fill()

            x += (length/rows)
            turtle.pendown()
            turtle.teleport(x, y)
            turtle.penup()
            num_len -= (length/rows)

        x = -0.5 * length
        y += (height / columns)
        turtle.teleport(x, y)
        num_hei -= (height/columns)

hirst_dots(bob, 10, 10, 500, 500, 10)




screen.exitonclick()