import turtle
from turtle import TK
import time
import random


WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'brown', 'cyan', 'purple', 'pink']


def get_number_of_racers():
    racers = 0
    while True:
        racers = turtle.textinput("","Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            TK.messagebox.showinfo(message="Input is not numeric.... Try Again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            TK.messagebox.showinfo(message="Number not in range 2-10. Try Again!")


def create_turtle(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1) 
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


while True:
    racers = get_number_of_racers()
    init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(colors)
    TK.messagebox.showinfo(message=f"The winner is {winner}")
    turtle.clearscreen()
    #time.sleep(5)