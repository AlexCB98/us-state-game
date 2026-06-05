import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv('50_states.csv')
states_name = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Name a state's name: "
    )

    if user_answer is None:
        break

    user_answer = user_answer.title()

    if user_answer == 'Exit':
        missing_states = [state for state in states_name if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('States_to_learn.csv')
        break

    if user_answer in states_name:
        state_data = data[data.state == user_answer]
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])

        writer.goto(x, y)
        writer.write(user_answer)

        guessed_states.append(user_answer)



