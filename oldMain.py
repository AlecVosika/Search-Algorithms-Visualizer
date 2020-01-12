import pygame
import time
import sys
from queue import Queue

def main(grid):
    # Main loop. Runs until the user hit the close button
    while running == True:
        for event in pygame.event.get():  # For every event the user does
            if event.type == pygame.QUIT:  # If user clicked close
                quit()  # Closes the program
            try:
                # Code for placing walls
                if pygame.mouse.get_pressed()[0]: # If the user holds left click
                    pos = pygame.mouse.get_pos() # Gets the mouse position
                    column = pos[0] // (WIDTH + MARGIN) # Change the x screen coordinate to grid coordinate
                    row = pos[1] // (HEIGHT + MARGIN) # Change the y screen coordinate to grid coordinate
                    grid[row][column] = 1 # Set that grid location to 1

                # Code for placing White spaces
                elif pygame.mouse.get_pressed()[2]: # If the user holds right click
                    pos = pygame.mouse.get_pos() # Gets the mouse position
                    column = pos[0] // (WIDTH + MARGIN) # Change the x screen coordinate to grid coordinate
                    row = pos[1] // (HEIGHT + MARGIN) # Change the y screen coordinate to grid coordinate
                    grid[row][column] = 0 # Set that grid location to 0
                    
                elif event.type == pygame.KEYDOWN: # If the user clicks a button
                    pos = pygame.mouse.get_pos() # Gets the mouse position
                    column = pos[0] // (WIDTH + MARGIN) # Change the x screen coordinate to grid coordinate
                    row = pos[1] // (HEIGHT + MARGIN) # Change the y screen coordinate to grid coordinate
                    # code for Placing the start position
                    if event.key == pygame.K_s: # if the button clicked was S
                        grid[row][column] = 2 # Set that grid location to 2
                        print("Start Grid coordinates:", row, column, end="\n\n")
                    # code for Placing the end position
                    elif event.key == pygame.K_e: # if the button clicked was F
                        grid[row][column] = 3 # Set that grid location to 3
                        print("End Grid coordinates:", row, column, end="\n\n")
                    # Debug code for printing the grid
                    elif event.key == pygame.K_g: # if the button clicked was G
                        print(grid, end="\n\n")
                    # code for BFS algorithm
                    elif event.key == pygame.K_1: # if the button clicked was 1
                        print("Starting BFS algorithm...", end="\n")
                        start = findStart(grid) # Finds start location
                        if start == None: # If start location does not exist
                            print("BFS canceled because start location was missing", end="\n\n")

                        else:
                            end = findEnd(grid)
                            if end == None: # If end location does not exist
                                print("BFS canceled because end location was missing", end="\n\n")

                            else: # If Start and End locations exist, run this
                                try:
                                    path = (BFS(grid, start, end)) # Gets the path coordinates
                                    for i in path:
                                        x,y = i
                                        grid[x][y] = 4 # Places path in grid
                                    print("Finished BFS algorithm.", end="\n\n")
                                except TypeError: # Needed if path is blocked
                                    print("No path found.", end="\n\n")
                                    removeVisualTrail(grid)
                    # Clears the board
                    elif event.key == pygame.K_0: # if the button clicked was 0
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
                    # preset maze 1
                    elif event.key == pygame.K_9: # if the button clicked was 9
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
                    # preset maze 2 
                    elif event.key == pygame.K_8: # if the button clicked was 8
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
                    # preset maze 3 
                    elif event.key == pygame.K_7: # if the button clicked was 7
                        grid =[
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], 
                            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], 
                            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], 
                            [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
                            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], 
                            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 1, 1, 1, 0, 3, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 0, 1, 1, 1, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0], 
                            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0], 
                            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0], 
                            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
                            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], 
                            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                        print("Loading preset 3", end="\n\n")
                        
            except IndexError: # needed to fix issue with hold click and mouse movement off screen
                pass
                    
        drawGrid(grid)

def drawGrid(grid):
    screen.fill(BLACK) # Set the screen background
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
            elif grid[row][column] == 5: # Used for visual trail
                color = BLUE

            draw = pygame.draw.rect(screen,
                        color,
                        [(MARGIN + WIDTH) * column + MARGIN,
                        (MARGIN + HEIGHT) * row + MARGIN,
                        WIDTH,
                        HEIGHT])

            drawText()

    clock.tick(60) # Limit to 60 frames per second
    pygame.display.flip() # Updates screen after drawing

def drawText():
    # render text
    keyBindsDict = {"Left click": "black",
                    "Right click": "white",
                    "S": "start",
                    "E": "end", 
                    "1": "BFS Algorithm"
                    }
    label = myfont.render("Key Binds", 0, (255,255,0))
    screen.blit(label, (875, 0))
    x,y = 821,20
    for key in keyBindsDict:
        label = myfont.render(key + " = " + keyBindsDict.get(key), 0, (255,255,255))
        screen.blit(label, (x, y))
        y += 20
    y += 20

    presetsDict = {"0": "clear grid",
                   "9": "maze preset 1",
                   "8": "maze preset 2",
                   "7": "maze preset 3",
                    }
    label = myfont.render("Layout presets", 0, (255,255,0))
    screen.blit(label, (855, y))
    y += 20
    for key in presetsDict:
        label = myfont.render(key + " = " + presetsDict.get(key), 0, (255,255,255))
        screen.blit(label, (x, y))
        y += 20    

def createGrid(grid):
    for row in range(20):
        grid.append([]) # Add an empty array that will hold each cell in this row
        for column in range(20):
            grid[row].append(0)  # Append a cell

def findStart(grid):
    print("    Finding start location...", end="\n")
    for row in range(len(grid)):
        for column in range(len(grid[0])):
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
    queue = [start]
    visited = set()

    while len(queue) != 0:
        if queue[0] == start:
            path = [queue.pop(0)]
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
    if spot[0]+1 >= 0 and spot[0]+1 <= 19 and spot[1]-1 >= 0 and spot[1]-1 <= 19: # down left
        spots.append((spot[0]+1, spot[1]-1)) 
    if spot[0]+1 >= 0 and spot[0]+1 <= 19 and spot[1]+1 >= 0 and spot[1]+1 <= 19: # down right
        spots.append((spot[0]+1, spot[1]+1))
    if spot[0]-1 >= 0 and spot[0]-1 <= 19 and spot[1]+1 >= 0 and spot[1]+1 <= 19: # up right
        spots.append((spot[0]-1, spot[1]+1))

    final = list()
    for i in spots:
        if grid[i[0]][i[1]] != 1 and i not in visited:
            final.append(i)
    return final

def removeVisualTrail(grid):
    for row in range(len(grid)):
        for column in range(len(grid[0])):
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
    WINDOW_SIZE = [1051, 821]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    # Sets font for instructions
    myfont = pygame.font.SysFont("monospace", 18)

    # Set title of screen
    pygame.display.set_caption("My App")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    running = True
    createGrid(grid)
    main(grid)
