import turtle
import random

GRID_SIZE = 6
CELL_SIZE = 80
SCREEN_SIZE = GRID_SIZE * CELL_SIZE
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.title("6x6 Turtle Maze")
wn.bgcolor("lightgray")

maze_drawer = turtle.Turtle()
maze_drawer.speed(0)
maze_drawer.hideturtle()
maze_drawer.color("black")
maze_drawer.pensize(2)
columns = turtle.Turtle()
rows = turtle.Turtle()

grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def generate_maze(x, y):
    grid[y][x] = 1

    directions = [(0, -1), (1, 0), (-1, 0)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx * 2, y + dy * 2 # Next cell to visit (jump over a wall)

        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[ny][nx] == 0:
            # Carve a path through the wall between current and next cell
            # The wall location is (x+dx, y+dy)
            # In this implementation, marking the cell as visited "removes" the wall

            # Move to the neighboring cell that was skipped over (the wall)
            grid[y + dy][x + dx] = 1 
            # Recursively call the function for the new cell
            generate_maze(nx, ny)

# Start generation from the top-left corner
generate_maze(0, 0)
# --------------------

# --- Drawing Function ---

def draw_maze():
    maze_drawer.penup()
    # Draw the outer boundary first
    maze_drawer.goto(0, 0)
    maze_drawer.pendown()
    for _ in range(4):
        maze_drawer.forward(SCREEN_SIZE)
        maze_drawer.right(90)
    maze_drawer.penup()
    
    # Draw internal walls based on the generated grid
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            cell_x = x * CELL_SIZE
            cell_y = y * CELL_SIZE
            
            # Check the "path" cell to the right (representing the left wall of next cell)
            if x < GRID_SIZE - 1 and grid[y][x+1] == 0:
                 # Draw vertical wall
                maze_drawer.goto(cell_x + CELL_SIZE, cell_y)
                maze_drawer.pendown()
                maze_drawer.goto(cell_x + CELL_SIZE, cell_y + CELL_SIZE)
                maze_drawer.penup()

            # Check the "path" cell below (representing the top wall of cell below)
            if y < GRID_SIZE - 1 and grid[y+1][x] == 0:
                # Draw horizontal wall
                maze_drawer.goto(cell_x, cell_y + CELL_SIZE)
                maze_drawer.pendown()
                maze_drawer.goto(cell_x + CELL_SIZE, cell_y + CELL_SIZE)
                maze_drawer.penup()

    # Define start and end points visually
    maze_drawer.color("green")
    maze_drawer.goto(CELL_SIZE * 0.5, CELL_SIZE * 0.5)
    maze_drawer.dot(CELL_SIZE * 0.4)
    
    maze_drawer.color("red")
    maze_drawer.goto(CELL_SIZE * (GRID_SIZE - 0.5), CELL_SIZE * (GRID_SIZE - 0.5))
    maze_drawer.dot(CELL_SIZE * 0.4)


draw_maze()
wn.tracer(1) # Re-enable updates to show


columns = [1,1,1,0,0,00,1,1,1,1]
rows = [1,1,1,0,0,1,1,0,0,1,1,1]





grid_columns = ()
grid_rows = ()

turtle.done()