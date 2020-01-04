import pygame
import time
import sys
from queue import Queue
from numpy.matrixlib.defmatrix import matrix

def main():
    # Loop until the user clicks the close button.
    while running == True:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                quit()  # Flag that we are done so we exit this loop

            if pygame.mouse.get_pressed()[0]: # Left Click
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                print(grid)
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)

            if pygame.mouse.get_pressed()[2]: # Right click
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                print(grid)
                grid[row][column] = 0
                print("Click ", pos, "Grid coordinates: ", row, column)
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    quit()

                if event.key == pygame.K_s:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    print(grid)
                    grid[row][column] = 2
                    print("Click ", pos, "Grid coordinates: ", row, column)

                if event.key == pygame.K_f:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    print(grid)
                    grid[row][column] = 3
                    print("Click ", pos, "Grid coordinates: ", row, column)

                if event.key == pygame.K_1:
                    start = findStart(grid)
                    print(start)
                    end = findEnd(grid)
                    print(end)
                    path = (BFS(grid, start, end))
                    print(path)
                    print(len(path))
                    for i in path:
                        x,y = i
                        grid[x][y] = 4


        drawGrid()

def drawGrid():
    # Set the screen background
    screen.fill(BLACK)
    # Draw the grid
    for row in range(10):
        for column in range(10):
            if grid[row][column] == 0:
                color = WHITE
                draw = pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
            elif grid[row][column] == 1:
                color = BLACK
                draw = pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
            elif grid[row][column] == 2:
                color = GREEN
                draw = pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
            elif grid[row][column] == 3:
                color = RED
                draw = pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
            elif grid[row][column] == 4:
                color = GREY
                draw = pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

def createGrid():
    for row in range(10):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(10):
            grid[row].append(0)  # Append a cell

def getadjacent(n):
    x,y = n
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

def findStart(maze):
    for row in range(len(maze)): # row
        for column in range(len(maze[0])): #column
            if maze[row][column] == 2:
                return tuple([row, column])

def findEnd(maze):
    for row in range(len(maze)):
        for column in range(len(maze[0])):
            if maze[row][column] == 3:
                return tuple([row, column])

def BFS(maze, start, end):
    basic_operations = 0
    queue = [start]
    visited = set()

    while len(queue) != 0:
        if queue[0] == start:
            path = [queue.pop(0)]  # Required due to a quirk with tuples in Python
        else:
            path = queue.pop(0)
        front = path[-1]
        if front == end:
            return path
        elif front not in visited:
            for adjacentSpace in getAdjacentSpaces(maze, front, visited):
                newPath = list(path)
                newPath.append(adjacentSpace)
                queue.append(newPath)
            
                basic_operations += 1
            visited.add(front)
    return None

def getAdjacentSpaces(maze, space, visited):
    spaces = list()
    if space[0]-1 >= 0 and space[0]-1 <= 9:
        spaces.append((space[0]-1, space[1]))  # Up
    if space[0]+1 >= 0 and space[0]+1 <= 9:
        spaces.append((space[0]+1, space[1]))  # Down
    if space[1]-1 >= 0 and space[1]-1 <= 9:    
        spaces.append((space[0], space[1]-1))  # Left
    if space[1]+1 >= 0 and space[1]+1 <= 9:
        spaces.append((space[0], space[1]+1))  # Right

    final = list()
    for i in spaces:
        if maze[i[0]][i[1]] != 1 and i not in visited:
            print(spaces)
            final.append(i)
    return final

def quit():
    pygame.quit()
    raise SystemExit(0)

if __name__ == "__main__" :

    start = (0,0)
    end = (9,9)

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GREY = (192,192,192)

    
    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 80
    HEIGHT = 80
    
    # This sets the margin between each cell
    MARGIN = 1

    # creates the grid list
    grid = []

    # Initialize pygame
    pygame.init()
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [811, 811]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    # Set title of screen
    pygame.display.set_caption("My App")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    running = True
    createGrid()
    main()
