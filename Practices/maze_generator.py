# MR 2nd Maze generator
# first we will import turtle and random
import turtle
import random
#we have to set the variables for the grid columns and the grid rows, and all the other details of the grid

num_cols = [[1,0,1,],[],[],[],[],[]]
grid_rows = [[],[],[],[],[],[]]
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

    for i in range(6): 
        current_y = starting_point_y - i * c_width
        t.penup()
        t.goto(start_point_x, current_y)
        t.pendown()
        t.forward(row_length)

    for i in range(6):
        t.penup()
        current_x = start_point_x + i * c_width
        t.goto(current_x, starting_point_y)
        t.pendown()
        t.right(90)
        t.forward(row_length) 
        t.left(90)
def mark_cells(grid_rows, row_heights, c_width, start_poin_x, starting_point_y):
    for row_index, row_data in range(grid_rows):
        for col_index, cell_value in range(row_data):
            if cell_value == 1:
                # Calculate the center position of the cell
                cell_center_x = start_point_x + col_index * c_width + c_width / 2
                cell_center_y = starting_point_y - row_index * row_heights - row_heights / 2
                t.penup()
                t.goto(cell_center_x, cell_center_y)
                t.pendown()

draw_complete_grid(
    grid_rows, 
    num_cols, 
    row_heights, 
    c_width, 
    start_point_x, 
    starting_point_y
)

# Mark the cells using the data structure
mark_cells(
    grid_rows, 
    row_heights, 
    c_width, 
    start_point_x, 
    starting_point_y
)



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
