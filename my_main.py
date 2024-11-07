from turtle import Turtle, Screen
from usstategame import USStateGame
import pandas

screen = Screen()
turtle = Turtle()
usstategame = USStateGame()

screen.title("U.S. States Game")
image = "python_practice_us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

usstategame.start_game()

screen.exitonclick()
