# MR 2nd Maze generator
# first we will import turtle and random
import turtle
import random
#we have to set the variables for the grid columns and the grid rows, and all the other details of the grid

num_cols = [[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]]

grid_rows = [[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]]
row_heights = 50
grid_width = 100
c_width  = 50
row_length = 250
start_point_x = -100
starting_point_y = 100

t = turtle.Turtle()
t.speed(5)
t.penup()

def draw_complete_grid(grid_rows, num_cols, row_heights, grid_width, start_point_x, starting_point_y):
    
    t.penup()
    t.goto(start_point_x, starting_point_y)
    t.pendown

    for i, row in enumerate(grid_rows):
        current_y = starting_point_y - i * c_width
        t.penup()
        t.goto(start_point_x, current_y)
        for columns in row:
            if columns == 1:
                t.pendown()
                t.forward(50)
            if columns == 0:
                t.penup()
                t.forward(50)

    t.right(90)
    for i, columns in enumerate(num_cols):
        current_x = start_point_x + i * c_width
        t.penup()
        t.goto(current_x, starting_point_y)
        for row in columns:
            if row == 1:
                t.pendown()
                t.forward(50)
            if row == 0:
                t.penup()
                t.forward(50)


draw_complete_grid(
    grid_rows, 
    num_cols, 
    row_heights, 
    c_width, 
    start_point_x, 
    starting_point_y
)

def maze_solvable(current_x, current_y, grid_rows, num_cols):
    



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
    turtle.done()
