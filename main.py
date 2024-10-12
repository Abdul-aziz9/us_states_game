import turtle
import pandas

# Author: AbdulAziz Oshinberu
# Date: 10/02/2024
# This application is helps people struggling with identifying the name of states in the U.S.
# Being an international student from Nigeria where the name of states are taught at an early stage in our educational system.
# Decided to use this game to teach myself the name of states.
# ENJOY!!


# This part of the code displays the screen of the application(The MAP of the U.S) 
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# This part of the code added the name of the states to the program
data = pandas.read_csv('50_states.csv')
state_list = data.state.to_list()

# This part of the code prepare to start the game and get every turtle ready
game_on = True
pet = turtle.Turtle()
pet.ht()
pet.penup()
answer_given = []

# This is where the code begins
while game_on:
    score = len(answer_given)
    answer = screen.textinput(f"{score}/50 Correct State", "Give A State Name").title()
    # This is the indentation for when the person leaves the game
    if answer == "Exit":
        samp = data.state.to_list()
        # list comprehended below
        state_dic = {'states you didn\'t mention': [state for state in samp if state not in answer_given]}
        # for state in samp:
        #     if state not in answer_given:
        #         state_dic['states you didn\'t mention'].append(state)
        nudata = pandas.DataFrame(state_dic)
        nudata.to_csv('states_to_learn.csv')
        game_on = False
        screen.bye()
    # This is the indentation for when the user is giving a name of a state 
    if answer in state_list:
        answer_given.append(answer)
        print(answer_given)
        row = data[data.state == answer]
        x = int(row.x)
        y = int(row.y)
        pet.goto(x, y)
        pet.write(f'{row.state.item()}', font=('Courier', 10, 'normal'))
        if score == 50:
            pet.goto(50, 100)
            pet.write('Completed', font=('Times New Roman', 60, 'normal'))
            game_on = False
turtle.mainloop()
