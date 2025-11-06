# MR 2nd Maze generator
# first we will import turtle and random
import turtle
import random
#we have to set the variables for the grid columns and the grid rows
grid_rows = [[1,2,3,],[4,5,6],[7,8,9]]
grid_columns = 6
start_point = (0,0)
end_point = (5,5)


turtle.pensize(10)
turtle.fillcolor("black")
turtle.begin_fill()
for x in range (6):
    turtle.forward(500)
    turtle.end_fill()
# we need at least 3 functions
# the first functions will be to randomly generate the grid columns with random open spaces in them

# In the function we will make a nested loop for the grid rows to be randomized with random spaces in them
# the second function will checking if the maze is solvable
# the functions will be checking if we have a starting point and if we have an end point
# the functions will use the path coordinates to check the correct wall coordinates in each direction
# after we make all the functions and set the variables we have to make a turtle
# we will use turtle to draw the maze
# we will code all the turtle setting so it looks like it is drawing the maze
# turtle always has to move the same way but if it over runs then we have to check that\
    turtle.penup()
    turtle.done()