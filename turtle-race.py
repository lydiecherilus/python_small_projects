import random
from turtle import Turtle, Screen

# seteup screen
screen = Screen()
screen.setup(width=500, height=500)
screen.title("Turtle Racing")

# take user bet
user_bet = screen.textinput(title="Bet: red, black, green, blue, purple \n", prompt="Which turtle will win the race? Enter a color: ")

if user_bet != "red" or user_bet != "black" or user_bet != "green" or user_bet != "blue" or user_bet != "purple":
    user_bet = screen.textinput(title="Bet: red, black, green, blue, purple \n", prompt="Which turtle will win the race? Enter a color: ")


screen.exitonclick()
