from turtle import Turtle
from turtle import Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="from 1 to 5, enter which turtle win")
colours = ["red", "green", "blue", "black", "brown"]
start_position = [50, 30, 10, -10, -30]
distance = [50, 60, 10, 15, 12, 20]
race_turtle_list = []


# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-100)

for i in range(0,5):
    turtle = Turtle(shape="turtle")
    turtle.color(colours[i])
    turtle.penup()
    turtle.goto(x=-230, y=start_position[i])
    race_turtle_list.append(turtle)
    print(len(race_turtle_list))
    print(turtle.color())
    print(turtle.position()[0])
name = []
for j in range(1,10):
    for i in race_turtle_list:
        move_distance = random.choice(distance)
        i.forward(move_distance)

        print(" move  #" + str(j) + " distance is: " + str(move_distance))
        print("current turtle X position is: " + str(i.position()[0]))
        if j ==9:
            name.append(i.position()[0])
            i.write("final position: " + str(move_distance))

winning_position = int(name.index(max(name)))+1

print("final position list")
print(name)
print("the " + str(winning_position) + " position turtle won!")
if winning_position == int(user_bet):
    print("you won the bet")
else:
    print("you didn't win the bet")










screen.exitonclick()
