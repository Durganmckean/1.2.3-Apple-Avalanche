import turtle as trtl
import random as rand

apple_image = "apple.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.bgpic("background.gif")

applelist = []
appleletters = []
letters = ['A', 'S', 'D', 'F']

for i in range(5):
    tempApple = trtl.Turtle()
    applelist.append(tempApple)
    appleletters.append(rand.choice(letters))

def draw_apple(index):

    global appleletter
    applelist[index].pu()
    applelist[index].shape(apple_image)
    wn.tracer(False)
    applelist[index].setx(rand.randint(-175,175))
    applelist[index].sety(rand.randint(-25,100))

    applelist[index].sety(applelist[index].ycor()-35)
    applelist[index].color("white")
    applelist[index].write(appleletters[index], align="center", font=("Arial", 40, "bold"))
    applelist[index].sety(applelist[index].ycor()+35)
    applelist[index].showturtle()
    wn.tracer(True)
    wn.update()

def drop_apple(index):
    applelist[index].pu()
    applelist[index].clear()
    applelist[index].sety(-150)
    applelist[index].hideturtle()
    appleletters[index] = rand.choice(letters)
    draw_apple(index)

def typedA():
    for i in range(5):
        if appleletters[i] == 'A':
            drop_apple(i)

def typedS():
    for i in range(5):
        if appleletters[i] == 'S':
            drop_apple(i)

def typedD():
    for i in range(5):
        if appleletters[i] == 'D':
            drop_apple(i)

def typedF():
    for i in range(5):
        if appleletters[i] == 'F':
            drop_apple(i)

for i in range(5):
    draw_apple(i)
wn.onkeypress(typedA, 'a')
wn.onkeypress(typedS, 's')
wn.onkeypress(typedD, 'd')
wn.onkeypress(typedF, 'f')

wn.listen()

wn.mainloop()

