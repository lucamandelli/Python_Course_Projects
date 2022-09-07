import turtle as t
import random


def geometry(Turtle, sides):
    for i in range(3, sides):
        Turtle.color(random_color())
        angle = 360 / i
        for j in range(i):
            Turtle.forward(100)
            Turtle.right(angle)

def dashed_line(Turtle):
    for i in range(20):
        Turtle.forward(10)
        Turtle.penup()
        Turtle.forward(10)
        Turtle.pendown()

def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    return (r, g, b)

def ran_walk(Turtle):
    directions = [0, 90, 180, 270]
    direction = 0
    for i in range(1000000):
        Turtle.color(random_color())
        last_direction = direction
        direction = random.choice(directions)
        not_proceed = True
        while not_proceed:
            if (direction == 90 and last_direction == 270) or (direction == 270 and last_direction == 90):
                direction = random.choice(directions)
            elif (direction == 0 and last_direction == 180) or (direction == 180 and last_direction == 0):
                direction = random.choice(directions)
            elif direction == last_direction:
                direction = random.choice(directions)
            else:
                not_proceed = False
        Turtle.setheading(direction)
        Turtle.forward(50)

def spirograph(Turtle, gap):
    for i in range(int(360 / gap)):
        Turtle.color(random_color())
        Turtle.circle(100)
        Turtle.setheading(Turtle.heading() + gap)


sh_list = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
winni_the_turtle = t.Turtle()
t.colormode(255)
winni_the_turtle.color(random_color())
winni_the_turtle.pensize(2)
winni_the_turtle.shape(random.choice(sh_list))
winni_the_turtle.speed(0)
spirograph(winni_the_turtle, 10)

screen = t.Screen()
screen.exitonclick()
