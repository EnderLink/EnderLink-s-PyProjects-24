from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()

#Movements and clear.
def change_angle_right():
    new_heading = bob.heading() - 10
    bob.setheading(new_heading)

def change_angle_left():
    new_heading = bob.heading() + 10
    bob.setheading(new_heading)

def going_forward():
    bob.forward(10)

def going_backward():
    bob.backward(5)

def clear():
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()


#Main running lines. Was slightly faulty for MY computer.
screen.listen()
screen.onkeypress(change_angle_left, "d")
screen.onkeypress(change_angle_right,"a")
screen.onkeypress(going_forward, "w")
screen.onkeypress(going_backward, "s")
screen.onkeypress(clear, "c")



screen.exitonclick()