import turtle
import pandas


screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv('50_states.csv')
state_list = data.state.to_list()


# def get_mouse_click(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click) to get co-ordinates
game_on = True
pet = turtle.Turtle()
pet.ht()
pet.penup()
answer_given = []

while game_on:
    score = len(answer_given)
    answer = screen.textinput(f"{score}/50 Correct State", "What's Another State Name").title()
    if answer == "Exit":
        samp = data.state.to_list()
        # list comprehended below
        state_dic = {'states you didn\'t mention': [state for state in samp if state not in answer_given]}
        # for state in samp:
        #     if state not in answer_given:
        #         state_dic['states you didn\'t mention'].append(state)
        nudata = pandas.DataFrame(state_dic)
        nudata.to_csv('states_to_learn.csv')
        break
    if answer in state_list:
        answer_given.append(answer)
        print(answer_given)
        row = data[data.state == answer]
        x = int(row.x)
        y = int(row.y)
        pet.goto(x, y)
        pet.write(f'{row.state.item()}', font=('Courier', 10, 'normal'))
        if score == 5:
            pet.write('Completed', font=('Courier', 10, 'normal'))
            game_on = False
turtle.mainloop()
