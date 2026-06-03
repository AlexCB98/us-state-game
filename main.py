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

user_answer = screen.textinput(title = 'Guess the State', prompt = "What's another state's name ?")

data = pandas.read_csv('50_states.csv')
states_name = data.state.to_list()



guessed_states = []

if user_answer in states_name:
    state_data = data[data.state == user_answer]
    x = int(state_data.x.iloc[0])
    y = int(state_data.y.iloc[0])

    writer.goto(x,y)
    writer.write(user_answer)
    guessed_states.append(user_answer)





turtle.mainloop()
