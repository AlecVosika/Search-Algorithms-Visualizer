import pygame
import time
import sys
from queue import Queue

"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""


def main(grid):
    # creates the grid list
 
    # Loop until the user clicks the close button.
    while running == True:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                quit()  # Flag that we are done so we exit this loop
            try:
                if pygame.mouse.get_pressed()[0]: # Left Click
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    grid[row][column] = 1

                if pygame.mouse.get_pressed()[2]: # Right click
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    grid[row][column] = 0
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        quit()

                    if event.key == pygame.K_s:
                        # User clicks the mouse. Get the position
                        pos = pygame.mouse.get_pos()
                        # Change the x/y screen coordinates to grid coordinates
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        # Set that location to one
                        grid[row][column] = 2
                        print("Start Grid coordinates:", row, column, end="\n\n")

                    if event.key == pygame.K_f:
                        # User clicks the mouse. Get the position
                        pos = pygame.mouse.get_pos()
                        # Change the x/y screen coordinates to grid coordinates
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        # Set that location to one
                        grid[row][column] = 3
                        print("End Grid coordinates:", row, column, end="\n\n")

                    if event.key == pygame.K_1:
                        print("Starting BFS algorithm...", end="\n")
                        start = findStart(grid)
                        if start == None:
                            print("BFS canceled because start location was missing", end="\n\n")

                        else:
                            end = findEnd(grid)
                            if end == None:
                                print("BFS canceled because end location was missing", end="\n\n")

                            else:
                                try:
                                    path = (BFS(grid, start, end))
                                    for i in path:
                                        x,y = i
                                        grid[x][y] = 4
                                    print("Finished BFS algorithm.", end="\n\n")
                                except TypeError:
                                    print("No path found.", end="\n\n")
                                    removeVisualTrail(grid)

                    if event.key == pygame.K_0: # Clears the board
                        grid = [
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                        print("clearing grid", end="\n\n")
                    if event.key == pygame.K_9: # preset maze 1
                        grid = [
                            [2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], 
                            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0], 
                            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
                            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]]
                        print("Loading preset 1", end="\n\n")
                    if event.key == pygame.K_8: # preset maze 2
                        grid = [
                            [2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
                            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], 
                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
                            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], 
                            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
                            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
                            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
                            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], 
                            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
                            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
                            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 3]]
                        print("Loading preset 2", end="\n\n")

            except IndexError:
                pass
                    

        drawGrid(grid)

def drawGrid(grid):
    # Set the screen background
    screen.fill(BLACK)
    # Draw the grid
    for row in range(20):
        for column in range(20):
            if grid[row][column] == 0:
                color = WHITE
            elif grid[row][column] == 1:
                color = BLACK
            elif grid[row][column] == 2:
                color = GREEN
            elif grid[row][column] == 3:
                color = RED
            elif grid[row][column] == 4:
                color = BLUE
            elif grid[row][column] == 5:
                color = BLUE

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

def createGrid(grid):
    for row in range(20):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(20):
            grid[row].append(0)  # Append a cell

def findStart(grid):
    print("    Finding start location...", end="\n")
    for row in range(len(grid)): # row
        for column in range(len(grid[0])): #column
            if grid[row][column] == 2:
                print("    Start location: ", str(tuple([row, column])), end="\n")
                return tuple([row, column])
    return None

def findEnd(grid):
    print("    Finding end location...", end="\n")
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 3:
                print("    End location: ", str(tuple([row, column])), end="\n")
                return tuple([row, column])
    return None

def BFS(grid, start, end):
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
            removeVisualTrail(grid)
            path = path[1:-1] # removes first and last coordinate in list
            return path
        elif front not in visited:
            for adjacentSpot in getAdjacentSpots(grid, front, visited):
                newPath = list(path)
                newPath.append(adjacentSpot)
                queue.append(newPath)

                x,y=adjacentSpot
                if grid[x][y] == 0:
                    grid[x][y] = 5
                    drawGrid(grid)
                    # time.sleep(1)

                basic_operations += 1
            visited.add(front)
    return None

def getAdjacentSpots(grid, spot, visited):
    spots = list()

    if spot[0]-1 >= 0 and spot[0]-1 <= 19: # Up
        spots.append((spot[0]-1, spot[1]))
    if spot[1]+1 >= 0 and spot[1]+1 <= 19: # Right
        spots.append((spot[0], spot[1]+1))
    if spot[0]+1 >= 0 and spot[0]+1 <= 19: # Down
        spots.append((spot[0]+1, spot[1]))
    if spot[1]-1 >= 0 and spot[1]-1 <= 19: # Left   
        spots.append((spot[0], spot[1]-1)) 
    if spot[0]-1 >= 0 and spot[0]-1 <= 19 and spot[1]-1 >= 0 and spot[1]-1 <= 19: # up left
        spots.append((spot[0]-1, spot[1]-1)) 
    if spot[0]-1 >= 0 and spot[0]-1 <= 19 and spot[1]+1 >= 0 and spot[1]+1 <= 19: # up right
        spots.append((spot[0]-1, spot[1]+1))
    if spot[0]+1 >= 0 and spot[0]+1 <= 19 and spot[1]+1 >= 0 and spot[1]+1 <= 19: # down right
        spots.append((spot[0]+1, spot[1]+1))
    if spot[0]+1 >= 0 and spot[0]+1 <= 19 and spot[1]-1 >= 0 and spot[1]-1 <= 19: # down left
        spots.append((spot[0]+1, spot[1]-1)) 

    final = list()
    for i in spots:
        if grid[i[0]][i[1]] != 1 and i not in visited:
            final.append(i)
    return final

def removeVisualTrail(grid):
    for row in range(len(grid)): # row
        for column in range(len(grid[0])): #column
            if grid[row][column] == 5:
                grid[row][column] = 0
    drawGrid(grid)

def quit():
    print("Closing application.")
    pygame.quit()
    raise SystemExit(0)

if __name__ == "__main__" :
    print("\n"*2)
    # creates the grid list
    grid = []

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GREY = (220,220,220)
    BLUE = (0,0,255)
    
    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 40
    HEIGHT = 40
    
    # This sets the margin between each cell
    MARGIN = 1

    # Initialize pygame
    pygame.init()
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [821, 821]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    # Set title of screen
    pygame.display.set_caption("My App")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    running = True
    createGrid(grid)
    main(grid)
