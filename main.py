"""import modules needed"""
import random
import turtle
from turtle import Turtle, Screen

"""setting up screen and colors """
timmy = Turtle()
screen = Screen()
turtle.colormode(255)
timmy.width(5)
color_list = [(245, 241, 233), (227, 234, 242), (245, 234, 239), (233, 242, 236), (208, 158, 96), (234, 213, 101),
              (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55),
              (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36),
              (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167),
              (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]

"""forward function"""
def move_forwards():
    timmy.forward(10)
    timmy.color(random.choice(color_list))


"""backward function"""
def move_backwards():
    timmy.backward(10)
    timmy.color(random.choice(color_list))


"""counter-clockwise function"""
def counter_clockwise():
    new = timmy.heading() - 10
    timmy.setheading(new)
    timmy.forward(10)
    timmy.color(random.choice(color_list))


"""clockwise function"""
def clockwise():
    new = timmy.heading() + 10
    timmy.setheading(new)
    timmy.forward(10)
    timmy.color(random.choice(color_list))

"""clear function"""
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


"""setting up the controlling keys"""
screen.listen()
screen.onkey(key='f', fun=move_forwards)
screen.onkey(key='b', fun=move_backwards)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear)
screen.onkey(key='a', fun=counter_clockwise)


"""setting up screen"""
screen.exitonclick()
