from guizero import App, Text, Waffle
import random

def addDot():
    print("tick")
    x = random.randint(0,dim-1)
    y = random.randint(0,dim-1)
    
    board.set_pixel(x,y, color)

def waffleClick(x, y):
    print(board.get_pixel(x,y))
    if board.get_pixel(x,y) == "red":
        print("destroy")
        board.set_pixel(x,y,"white")

app = App("Destroy the Dots")

instructions = Text(app, text="Click the dots to destroy them")

color= 'red'
dim = 5
time = 1000
board = Waffle(app, width=dim, height=dim, command=waffleClick)
board.repeat(time, addDot)

app.display()