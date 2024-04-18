from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States Game")
screen.setup(725,491)
screen.bgpic("Intermediate/U.S States Game/blank_states_img.gif")

data = pandas.read_csv("Intermediate/U.S States Game/50_states.csv")
guessed_states = 0
all_states = data.state.to_list()


while guessed_states < 50:
    answer_state = screen.textinput(title=f"{guessed_states}/50 States Correct",
                                    prompt="What's another state's name?").title()
   
    state_data = data[data.state == answer_state]
    # s = Turtle()
    # s.color("red")
    # s.hideturtle()
    # s.penup()
    if answer_state == "Exit":
        # for state in all_states:
            # if not state_data.empty:
            #     s.goto(int(state_data.x), int(state_data.y))
            #     s.write(state,align="center", font=("Arial", 8, "normal"))
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv("Intermediate/U.S States Game/States_to_learn.csv")
        break
    
    if not state_data.empty:
        guessed_states += 1
        t = Turtle()
        t.hideturtle()
        t.penup()
        # s.color("black")
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        all_states.remove(answer_state)


screen.exitonclick()
