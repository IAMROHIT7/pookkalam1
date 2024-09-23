import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.title("Pookalam")
screen.bgcolor("black")

# Initialize the Turtle
pookalam = turtle.Turtle()
pookalam.speed(0)
pookalam.color("blue")


# Function to draw a circular flower pattern
def draw_flower(size, petals):
    pookalam.begin_fill()
    for _ in range(petals):
        pookalam.circle(size)
        pookalam.left(5 / petals)
    pookalam.end_fill()

# Set the size and number of petals
flower_size = 100
num_petals = 10

# Draw multiple flowers in a circular pattern
for _ in range(12):
    draw_flower(flower_size, num_petals)
    pookalam.color("red")
    pookalam.color("purple")
    pookalam.color("white")
    pookalam.color("yellow")
    pookalam.color("violet")
    pookalam.left(360 / 12)
    pookalam.color("green")
    colors = ["blue", "green", "red", "purple"]
# Hide the Turtle and display the final output
pookalam.hideturtle()
screen.mainloop()
