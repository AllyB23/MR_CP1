# MR 2nd Starter
import turtle


def draw_branch(length):
    if length >5:
        for i in range(3):
            turtle.forward(length)
            draw_branch(length / 3)
            turtle.back(length)
            turtle.right(60)


turtle.speed(7)
turtle.color("light blue")
turtle.penup
turtle.goto(10,10)
turtle.pendown

for i in range(6):
    draw_branch(100)
    turtle.right(60)



