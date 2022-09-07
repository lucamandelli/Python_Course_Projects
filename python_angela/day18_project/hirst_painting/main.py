import random
import colorgram
import turtle as t

def paint(Turtle, color_list, num_dot):
    Turtle.penup()
    Turtle.hideturtle()
    Turtle.setheading(225)
    Turtle.forward(300)
    Turtle.setheading(0)
    for dot_count in range(1, num_dot + 1):
        Turtle.forward(50)
        Turtle.dot(20, random.choice(color_list))
        if dot_count % 10 == 0:
            Turtle.setheading(90)
            Turtle.forward(50)
            Turtle.setheading(180)
            Turtle.forward(500)
            Turtle.setheading(0)

colors = colorgram.extract("C:\\Users\\lucap\\OneDrive\\Documentos\\GitHub\\Python_Course_Projects\\python_angela\\day18_project\\hirst_painting\\image.jpg", 30)
rgb_colors = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
t.colormode(255)
screen = t.Screen()
screen.screensize()
winni = t.Turtle()
winni.speed(0)
winni.shapesize(1)

paint(winni, rgb_colors, 100)






screen.exitonclick()
