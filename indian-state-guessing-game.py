import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("India States Game")
img = "statesimg.gif"
screen.bgcolor("gray")
screen.addshape(img)
t.shape(img)
screen.setup(width=770, height=825)
writer = t.Turtle()
writer.hideturtle()
writer.penup()

data = pd.read_csv("state.csv")
states = data['State'].str.lower().tolist()
gs = []
score = 0
while len(gs) < 35:
    ans_user = screen.textinput(title=f"Guess the State({score}/33)", prompt="What is another state?").lower()

    if ans_user == "exit":
        ms = [state for state in states if state not in gs]
        nd = pd.DataFrame(ms)
        nd.to_csv("missing-state.csv", index=False)
        screen.bye()
        break

    if ans_user in states:
        gs.append(ans_user)
        x = data[data["State"] == ans_user].x.iloc[0]
        y = data[data["State"] == ans_user].y.iloc[0]
        writer.goto(x, y)
        writer.write(ans_user)
        score += 1







