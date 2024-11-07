from turtle import Turtle, Screen
import pandas

screen = Screen()


class USStatesGame(Turtle):
    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv("python_practice_us_states_game/50_states.csv")
        # Turn state column/series of data into a list
        self.all_states = self.data.state.to_list()
        self.guessed_states = []

    def get_state_input(self):
        # -- title of input, keep track of number correct out of 50
        return screen.textinput(
            f"{len(self.guessed_states)}/50 Correct", "Enter Name of State:"
        ).lower()

    def start_game(self):
        while len(self.guessed_states) < 50:
            # 1. ask input: make sure to turn input string into lower case
            state_input = self.get_state_input()
            # print(f"check state_input value: {state_input}")

            # Exit the game if user types "exit"
            if state_input == "exit":
                # populate all of the states that the user missed
                print("User chose to exit")

                # find missing states using list comprehension instead
                missing_in_guessed_states_list = [
                    state
                    for state in self.all_states
                    if state not in self.guessed_states
                ]
                new_data = pandas.DataFrame(
                    {"States to Learn": missing_in_guessed_states_list}
                )
                new_data.to_csv(
                    "python_practice_us_states_game/states_to_learn.csv", index=False
                )
                break

            # 2. check Answer
            if state_input in [state.lower() for state in self.all_states]:
                self.guessed_states.append(state_input)
                # -- populateOnMap(x,y) by creating a new turtle text object
                map = Turtle()
                map.hideturtle()
                map.penup()
                # locate x an y coordinate from 50 csv file
                state_data = self.data[self.data.state.str.lower() == state_input]
                map.goto(state_data.x.item(), state_data.y.item())
                map.write(state_data.state.item())

        print("Game Over")
