from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
suser_bet = screen.textinput("Make your bet", "Which turtle will wni the race? Enter a color: ")

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
turtlse = []

starting_pos = 100
for i in colors:
    tturtle = Turtle()
    tturtle.color(i)
    tturtle.shape("turtle")
    tturtle.speed(2)

    tturtle.penup()
    tturtle.goto(-210, starting_pos)
    starting_pos -= 100/4
    turtlse.append(tturtle)

if suser_bet:
    is_race_on = True

winner = 0
for turtle in turtlse:
    print(turtle.pencolor())
    print(suser_bet)
    print(turtle)
    if turtle.pencolor() in suser_bet:
        suser_bet = turtle

while is_race_on:

    for turtle in turtlse:
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

        xcor = turtle.xcor()
        if turtle.xcor() >= 200:
            winner = turtle.pencolor()
            is_race_on = False

if suser_bet == winner:
    print(f"The {winner.color} turtle won! You were right!")
else:
    print("You lost!")

screen.bye()