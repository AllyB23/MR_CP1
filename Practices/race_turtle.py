# MR 2nd Turtle Race
import turtle
import random

t1= turtle.Turtle()
t2= turtle.Turtle()
t3= turtle.Turtle()
t4= turtle.Turtle()
t5= turtle.Turtle()

t1.color("red")
t1.pensize(3)
t1.shape("turtle")
t1.penup()
t1.goto(0, 100)

t2.color("yellow")
t2.pensize(3)
t2.shape("turtle")
t2.penup()
t2.goto(0, 50)

t3.color("Pink")
t3.pensize(3)
t3.shape("turtle")
t3.penup()
t3.goto(0, 0)

t4.color("Purple")
t4.pensize(3)
t4.shape("turtle")
t4.penup()
t4. goto(0, -50)

t5.color("green")
t5.pensize(3)
t5.shape("turtle")
t5.penup()
t5.goto(0, -100)

finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(500, - 300)
finish_line.pendown()
finish_line.setheading(90)
finish_line.forward(600)

t1.goto(random.randint(100, 100), random.randint(100, 100))
t2.goto(random.randint(100, 50), random.randint(100, 50))
t3.goto(random.randint(100, 0), random.randint(100, 0))
t4.goto(random.randint(100, -50), random.randint(100, -50))
t5.goto(random.randint(100, -100), random.randint(100, -100))


turtle.done()

