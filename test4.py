import sys
import time
import math
from queue import Queue
from PIL import Image

# -m pip install imageio --user
import imageio


def iswhite(value):
    if value == (255,255,255) or value == (0,255,0) or value == (255,0,0): 
        return True

def getadjacent(n):
    x,y = n
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1),
            (x-1,y-1),(x+1,y-1),(x+1,y+1),(x-1,y+1)]

def BFS(start, end, pixels):
    # Used for the gif creation
    count = 0
    gif = []
    print(pixels[2,2])
    queue = Queue()
    queue.put([start]) # Wrapping the start tuple in a list

    while not queue.empty():

        path = queue.get() 
        pixel = path[-1]

        if pixel == end:
            imageio.mimsave('C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\gif.gif', gif)
            return path

        for adjacent in getadjacent(pixel):
            x,y = adjacent

            if iswhite(pixels[x,y]):
                pixels[x,y] = (127,127,127) # Marks a white visited pixel grey. This
                                            # removes the need for a visited list.
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)

                # Count is used for gif creation
                count = count + 1
                # Used to save the grayed image and create a gif
                if count % 2000 == 0:
                    base_img.save("C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\grey_img.png")
                    gif.append(imageio.imread("C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\grey_img.png"))

    imageio.mimsave('C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\gif.gif', gif)
    quit("Error: no path was found.")

def findStartAndEnd(image):
    convertedImg = Image.open(image)
    (width,height) = convertedImg.size
    startX = 0
    startY = 0
    startTotalPX = 0
    endX = 0
    endY = 0
    endTotalPX = 0
    for x in range(width):
        for y in range(height):
            color = convertedImg.getpixel((x,y))
            if color == (0,255,0):
                startX += x
                startY += y
                startTotalPX += 1
                convertedImg.putpixel((x, y), (255,255,255))
            if color == (255,0,0):
                endX += x
                endY += y
                endTotalPX += 1
                convertedImg.putpixel((x, y), (255,255,255))
            
    start = (int((startX / startTotalPX)),int((startY / startTotalPX)))
    end = (int((endX / endTotalPX)),int((endY / endTotalPX)))
    return start,end

def convertImg(image):
    # Opens the original image and prints its size
    originalImg = Image.open(image)
    # Gets width and height of the originalImg for printing & resizing purposes
    (width,height) = originalImg.size
    print("Image size: " + str(width) + " x " + str(height))

    # Creates a resized image of the original if its taken from phone
    if (width,height) == (1920, 1080):
        resizedImg = originalImg.resize((480, 270), Image.ANTIALIAS)
    # Sets resizedImg variable to the original image
    else:
        resizedImg = originalImg

    # Saves and opens resizedImg for writing to
    resizedImg.save("C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\resizedImg.png")
    resizedImg = Image.open("C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\resizedImg.png")
    # sets width and height to the resizedImg
    (width,height) = resizedImg.size
    print("Downscaled image size: " + str(width) + " x " + str(height))

    # Creates the converted image to place the new pixels in
    convertedImg = Image.new('RGB', (width, height))
    
    for x in range(width):
        for y in range(height):
            color = resizedImg.getpixel((x,y))
            # Puts a black border around the image
            if (x == 0 or y == 0 or x == width - 1 or y == height - 1):
                convertedImg.putpixel((x, y), (0,0,0))
                continue
            # Checks for green color range and converts to solid green
            if (color[0] >= 0 and color[0] <= 50) and (color[1] >= 90) and (color[2] >= 0 and color[2] <= 120):
                convertedImg.putpixel((x, y), (0,255,0))
                continue
            # Checks for red color range and converts to solid red
            if (color[0] >= 95) and (color[1] >= 0 and color[1] <= 50) and (color[2] >= 0 and color[2] <= 60):
                convertedImg.putpixel((x, y), (255,0,0))
                continue
            # converts eny color whose RGB value is less than 225 to white
            if (color[0] >= 90) or (color[1] >= 170) or (color[2] >= 170):
                convertedImg.putpixel((x, y), (255,255,255)) 
                continue
            # converts any color whose RGB value is higher than 225 to black
            if any(z < 225 for z in color):
                convertedImg.putpixel((x, y), (0,0,0))
                continue

    convertedImg.save("C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\convertedImg.png")



if __name__ == '__main__':
    # Converts all colors to be either black, white, red, or green
    convertImg("C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\img.png")

    # locates the center of the green and red dots
    start,end  = findStartAndEnd("C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\convertedImg.png")
    distanceX = start[0]
    distanceY = start[1]
    
    
    # Starts timer
    timerStart = time.process_time()

    # Opens and loads the image
    base_img = Image.open("C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\convertedImg.png")
    base_pixels = base_img.load()

    # Runs the Breadth-First Search (BFS) algorithm
    print("Start Coordinate: " + str(start))
    print("End Coordinate: " + str(end), end="\n\n")
    path = BFS(start, end, base_pixels)

    # Saves a greyed out version for trouble-shooting purposes
    base_img.save("C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\grey_img.png")

    # Opens the original image agian to print the fastest path
    path_img = Image.open("C:\\Users\\Alecv\\Documents\\CodeRepository\\Github\\Search-Algorithms-Visualizer\\convertedImg.png")
    path_pixels = path_img.load()

    # Prints the fastest path in blue
    for position in path:
        x,y = position
        path_pixels[x,y] = (0,0,255)
        