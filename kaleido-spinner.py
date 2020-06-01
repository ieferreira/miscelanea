from turtle import *
import random
# based on a previous code, plain spinner with only 3 rings
print("PRESS SPACE TO MAKE IT SPIN!")
n = int(input("input the number of rings on the spinner (1 to whatever you want... but after ~60 it looks way trippy than it should)"))
win = Screen()
win.title("KaleidoSpinner!")
win.bgcolor("white")
state = {"turn":1}

def spinner():
    global n
    clear()
    angle = state["turn"]/10
    right(angle)
    pensize(100/n) 
    int_ang = 360/n
    forward(100)
    colors =  ["blue", "yellow","green", "red", "cyan", "red", "orange", "violet"]
    pencolor(random.choice(colors)) # deactivate if you want the body of the spinner to be black
    for i in range(1,n+1):               
        dot(int_ang,random.choice(colors))
        back(100)
        right(int_ang)
        forward(100)
    back(100)
    right(int_ang)
    update()

def animate():
    if state["turn"]>0:
        state["turn"] -= 1
    spinner()
    ontimer(animate,20)

def flick():
    state["turn"] += 30

setup(420,420,370,0)
hideturtle()
tracer(False)
width(20)

onkey(flick, "space")
listen()
animate()
win.mainloop()