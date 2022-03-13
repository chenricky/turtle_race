from turtle import Turtle
from turtle import Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color of your choice")
colours = ["red", "green", "blue", "black", "brown"]
start_position = [50, 30, 10, -10, -30]

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-100)

for i in range(0, 5):
    turtle = Turtle(shape="turtle")
    turtle.color(colours[i])
    turtle.penup()
    turtle.goto(x=-230, y=start_position[i])

screen.exitonclick()
