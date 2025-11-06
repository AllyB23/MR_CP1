import turtle
import random

# --- Configuration Variables ---
GRID_ROWS_COUNT = 6
GRID_COLS_COUNT = 6
START_POINT = (0, 0)
END_POINT = (5, 5) # Adjusted to be 0-indexed (row 5, column 5)

# Variables for the maze representation
maze_wall_char = '#'
maze_path_char = ' '

# Global variable to store the generated grid
maze_grid = []

# --- Function Definitions ---

def generate_random_grid():
    """
    Generates a 2D grid using the global configuration variables,
    filled randomly with walls and open paths.

    Returns:
        list of list: A 2D list representing the maze grid.
    """
    grid = []
    # Use the variable defined earlier for the number of rows
    for r in range(GRID_ROWS_COUNT):
        row = []
        # Use the variable defined earlier for the number of columns
        for c in range(GRID_COLS_COUNT):
            # Randomly decide if a cell is a path or a wall using our variables
            if random.random() < 0.7: # 70% chance of being a path
                row.append(maze_path_char)
            else:
                row.append(maze_wall_char)
        grid.append(row)

    # Ensure start and end points are always open paths
    grid[START_POINT[0]][START_POINT[1]] = maze_path_char
    grid[END_POINT[0]][END_POINT[1]] = maze_path_char
    
    return grid

def is_maze_solvable(grid, start, end):
    """
    Checks if a path exists from start to end using Breadth-First Search (BFS)
    without using the collections module (uses a standard list as a queue).
    """
    rows = len(grid)
    cols = len(grid)
    # Using a standard Python list as a queue (FIFO)
    queue = [start] 
    visited = set([start])
    
    # Possible movements: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        # Use list.pop(0) to get the first element (FIFO behavior)
        current_r, current_c = queue.pop(0) 
        
        if (current_r, current_c) == end:
            return True

        for dr, dc in directions:
            next_r, next_c = current_r + dr, current_c + dc
            
            # Check if the next cell is within bounds and not a wall using our variables
            if 0 <= next_r < rows and 0 <= next_c < cols and \
               grid[next_r][next_c] == maze_path_char and \
               (next_r, next_c) not in visited:
                
                visited.add((next_r, next_c))
                # Use list.append() to add to the end of the queue
                queue.append((next_r, next_c)) 
                
    return False

def draw_maze(grid, cell_size=30):
    """
    Uses the turtle library to draw the generated maze grid.
    """
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width=len(grid) * cell_size + 50, height=len(grid) * cell_size + 50)
    screen.bgcolor("white")
    t.speed(0) # Fastest drawing speed
    t.hideturtle()
    t.penup()

    # Calculate initial position to center the maze
    start_x = -(len(grid) * cell_size) / 2
    start_y = (len(grid) * cell_size) / 2

    for r in range(len(grid)):
        for c in range(len(grid)):
            x = start_x + c * cell_size
            y = start_y - r * cell_size
            
            t.goto(x, y)
            t.pendown()
            
            # Use our variable to check for a wall
            if grid[r][c] == maze_wall_char:
                t.fillcolor("black")
                t.begin_fill()
                for _ in range(4):
                    t.forward(cell_size)
                    t.right(90)
                t.end_fill()
            elif (r, c) == START_POINT:
                t.fillcolor("green") # Start point color
                t.begin_fill()
                for _ in range(4):
                    t.forward(cell_size)
                    t.right(90)
                t.end_fill()
            elif (r, c) == END_POINT:
                t.fillcolor("red") # End point color
                t.begin_fill()
                for _ in range(4):
                    t.forward(cell_size)
                    t.right(90)
                t.end_fill()
            
            t.penup()

    print(f"Start point: {START_POINT}, End point: {END_POINT}")


# --- Main Logic ---

# 1. Generate the grid repeatedly until a solvable one is found
while True:
    # Call the function to generate a grid using the global variables
    maze_grid = generate_random_grid() 
    if is_maze_solvable(maze_grid, START_POINT, END_POINT):
        print("Solvable maze generated.")
        break
    else:
        continue

# 2. Draw the solvable maze
draw_maze(maze_grid)

# 3. Keep the turtle window open until manually closed
turtle.done()