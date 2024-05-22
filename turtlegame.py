from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_game_on = False
guess = screen.textinput(title="Your bet", prompt="Enter the color of your turtle(colors:blue, black, green, red, purple, orange):")
color = ['red', 'blue', 'green', 'orange', 'purple', 'black']
y_position = [-100, -50, 0, 50, 100, 150]
all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if guess:
    is_game_on = True
while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == guess:
                print(f"You've won, the {winning_color} is the winner!!")
            else:
                print(f"you've lost, the {winning_color} is the winner!!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
