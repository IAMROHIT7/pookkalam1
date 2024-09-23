import turtle
import random

# Set up screen
win = turtle.Screen()
win.bgcolor("yellow")

# Create turtle object
pookalam = turtle.Turtle()
pookalam.speed(0)

# Function to draw a flower
def draw_flower(turt, x, y, radius, color):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.fillcolor(color)
    turt.begin_fill()
    for _ in range(10):
        turt.circle(radius)
        turt.left(36)
    turt.end_fill()

# Function to draw Pookalam
def draw_pookalam():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    radius = 100
    for i in range(1):
        for j in range(1):
            draw_flower(pookalam, j*50 - 100, i*50 - 100, radius, random.choice(colors))

# Draw Pookalam
draw_pookalam()

# Keep the window open
turtle.done()