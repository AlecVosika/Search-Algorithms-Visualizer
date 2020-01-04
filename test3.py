import pygame
import time
import sys
from queue import Queue

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
                color = GREEN
                draw = pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
            elif grid[row][column] == 9:
                color = RED
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

def quit():
    pygame.quit()
    raise SystemExit(0)

def iswhite(value):
    if value == (255,255,255) or value == (0,255,0) or value == (255,0,0): 
        return True

def getadjacent(n):
    x,y = n
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

def BFS(row, column):
    queue = Queue()
    queue.put([start]) # Wrapping the start tuple in a list

    while not queue.empty():

        path = queue.get() 
        pixel = path[-1]

        if pixel == end:
            return path

        for adjacent in getadjacent(pixel):
            x,y = adjacent
            if grid[x][y] == 0:
                grid[x][y] = 9 # Marks a white visited pixel grey. This
                                            # removes the need for a visited list.
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)
            drawGrid()  
            print(path) 
        time.sleep(1) 

def main():
    # Loop until the user clicks the close button.
    while running == True:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                quit()  # Flag that we are done so we exit this loop
            if pygame.mouse.get_pressed()[0]:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                print(grid)
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
            if pygame.mouse.get_pressed()[2]:
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
                if event.key == pygame.K_1:
                    BFS(row, column)

        drawGrid()

if __name__ == "__main__" :

    start = (0,0)
    end = (9,9)

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    
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
