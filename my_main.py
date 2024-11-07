from turtle import Turtle, Screen
from usstatesgame import USStatesGame
import pandas

screen = Screen()
turtle = Turtle()
usstatesgame = USStatesGame()

screen.title("U.S. States Game")
image = "python_practice_us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

usstatesgame.start_game()

screen.exitonclick()
