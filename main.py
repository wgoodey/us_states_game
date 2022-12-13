import turtle
from turtle import Screen, Turtle
import pandas

# get 50 states data from file as dataframe
data = pandas.read_csv("50_states.csv")

# setup screen
screen = Screen()
screen.title("US States Game")
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")

writer = Turtle()
writer.penup()
writer.hideturtle()

correct_guesses = []

while len(correct_guesses) < 50:
    # get a guess from user
    try:
        guess = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                 prompt="Guess the name of a state.")
        guess = guess.title()
    except AttributeError:
        break
    try:
        if guess in correct_guesses:
            pass
        else:
            state_info = data[data.state == guess]
            writer.goto(int(state_info.x), int(state_info.y))
            writer.write(state_info.state.item(), align="center")
            correct_guesses.append(state_info.state.item())
    except TypeError:
        print(f"{guess} is not a state in the USA.")

writer.goto(0, 0)
writer.color("red")
if len(correct_guesses) == 50:
    writer.write(f"You got all 50 states!", align="center", font=("Arial", 20, "normal"))
else:
    writer.write(f"You got {len(correct_guesses)} states!", align="center", font=("Arial", 20, "normal"))
# TODO: export csv of states that were missed.
all_states = list(data.state)
missed_states = []
for state in all_states:
    if state not in correct_guesses:
        missed_states.append(state)

missed_states = pandas.DataFrame(missed_states)
missed_states.to_csv("states_to_learn.csv")

screen.exitonclick()
