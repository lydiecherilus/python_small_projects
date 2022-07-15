import random
from turtle import Turtle, Screen

# seteup screen
screen = Screen()
screen.setup(width=500, height=500)
screen.title("Turtle Racing")

# create game over functionality
game_over = Turtle()
game_over.hideturtle()
game_over.penup()
game_over.goto(-230, 140)
game_over.color("deep pink")

# take user bet
user_bet = screen.textinput(title="Bet: red, black, green, blue, purple \n", prompt="Which turtle will win the race? Enter a color: ")
    
# turtles color and position
turtles_colors = ["red", "black", "green", "blue", "purple"]
y_positions = [-120, -60, 0, 60, 120]
all_turtles = []

# create turtles
for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtles_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
    
is_race_on = False
# check if user bet exists and set is_race_on to True
if user_bet:
    is_race_on = True

# start race
while is_race_on:
    for turtle in all_turtles:
        # if a turtle crosses the finish line, the game is over
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                game_over.write(f"You bet on {user_bet}.\nYou win! The {winning_color} turtle is the winner!", font=("Arial", 15, "bold"))
            else:
                game_over.write(f"You bet on {user_bet}.\nYou lost. The {winning_color} turtle is the winner!", font=("Arial", 15, "bold"))
        random_distance = random.randint(0, 12)
        turtle.forward(random_distance)
        

screen.exitonclick()
