#20x20 grid

import pygame
import random
import time

#default values of grid size and starting pattern
patternSelection = 5
size = 16

#Default screen size
WINDOW_SIZE = [800, 800]


grid = []
tracker = []
pattern = []


def rotate_and_center(ds, x, y, image, degrees):
    #rotating a square
    global screen
    rotated = pygame.transform.rotate(image, degrees)
    rect = rotated.get_rect()
    screen.blit(rotated, (x - rect.center[0], y - rect.center[1]))

def printGrid(grid):
    #pretty printing of grid
    for row in grid:
        print(row)
    print("\n")


def drawGrid(grid):
    global screen
    # Draw the grid
    for row in range(len(grid)):
        for column in range(len(grid)):
            if grid[row][column] == 0:
                img = pygame.image.load('curves_v.bmp')
                color = WHITE
            if grid[row][column] == 1:
                img = pygame.image.load('curves_h.bmp')
                color = BLACK
            pygame.draw.rect(screen, color,[(WIDTH) * column, (HEIGHT) * row, WIDTH, HEIGHT]) #backup in case of image not loading
            screen.blit(pygame.transform.scale(img, (int(WIDTH), int(HEIGHT))), (int(HEIGHT * column), int(HEIGHT * row)))


def updateSquare(row,column):
    #draw single square
    if grid[row][column] == 0:
        img = pygame.image.load('curves_v.bmp')
        color = WHITE
    if grid[row][column] == 1:
        img = pygame.image.load('curves_h.bmp')
        color = BLACK
    pygame.draw.rect(screen, color,[(WIDTH) * column, (HEIGHT) * row, WIDTH, HEIGHT])  # backup in case of image not loading
    screen.blit(pygame.transform.scale(img, (int(WIDTH), int(HEIGHT))), (int(HEIGHT * column), int(HEIGHT * row)))


def createGrid(size):
    #create grid of a given size with random 1's & 0's
    global grid
    grid = []
    for i in range(size):
        row = []
        for x in range(size):
            row.append(random.randrange(2))
        grid.append(row)


def createTracker():
    #create a grid of references to keep track of which elements have been changed
    global grid
    global tracker

    for rowIndex in range(0,len(grid)):
        row = []
        for cellIndex in range(0, len(grid)):
            row.append([rowIndex,cellIndex])
        tracker.append(row)


def stripTracker(pattern):
    #strip the tracking grid of any references where the element is already the correct value
    global grid
    global tracker

    correct = []

    if tracker != []:
        for rowIndex, row in enumerate(tracker):
            for refIndex, ref in enumerate(row):
                if grid[ref[0]][ref[1]] == pattern[ref[0]][ref[1]]:
                    correct.append(ref)

        for rowIndex, row in enumerate(tracker):
            newRow = [e for e in row if e not in correct]
            tracker[rowIndex] = newRow
            if tracker[rowIndex] == []:
                del tracker[rowIndex]


def createPattern(patternNumber):
    #create a grid with a set pattern
    global grid
    global pattern
    value = 1

    if patternNumber == 0:
        # create a grid of all 0's
        for i in range(0,len(grid)):
            row = []
            for x in range(0,len(grid)):
                row.append(0)
            pattern.append(row)
        return pattern

    elif patternNumber == 1:
        # create a grid of all 1's
        for i in range(0, len(grid)):
            row = []
            for x in range(0, len(grid)):
                row.append(1)
            pattern.append(row)
        return pattern

    elif patternNumber == 2:
        #create a grid of alternating 1's and 0's
        firstValue = 1
        for i in range(0, len(grid)):
            row = []
            value = firstValue
            for x in range(0, len(grid)):
                if value == 1:
                    row.append(value)
                    value = 0
                else:
                    row.append(value)
                    value = 1
            pattern.append(row)

            if firstValue == 1:
                firstValue = 0
            else:
                firstValue = 1
        return pattern

    elif patternNumber == 3:
        #create a grid of alternating 1's and 0's starting on 1
        for i in range(0, len(grid)):
            row = []
            value = 1
            for x in range(0, len(grid)):
                if value == 1:
                    row.append(value)
                    value = 0
                else:
                    row.append(value)
                    value = 1
            pattern.append(row)
        return pattern

    elif patternNumber == 4:
        #create a grid of alternating lines of 1's and 0's
        for i in range(0, len(grid)):
            row = []
            if value == 1:
                for x in range(0, len(grid)):
                    row.append(value)
                value = 0
            else:
                for x in range(0, len(grid)):
                    row.append(value)
                value = 1
            pattern.append(row)
        return pattern

    elif patternNumber == 5:
        #create a grid of alternating 1's and 0's starting on 0
        for i in range(0, len(grid)):
            row = []
            value = 0
            for x in range(0, len(grid)):
                if value == 1:
                    row.append(value)
                    value = 0
                else:
                    row.append(value)
                    value = 1
            pattern.append(row)
        return pattern

    elif patternNumber == 6:
        #create a grid of alternating 11's and 00's
        firstValue = 1
        for i in range(0, len(grid)):
            row = []
            value = firstValue
            repeat = True
            for x in range(0, len(grid)):
                if value == 1 and repeat == False:
                    row.append(value)
                    value = 0
                    repeat = True
                elif value == 1 and repeat == True:
                    row.append(value)
                    repeat = False
                elif value == 0 and repeat == False:
                    row.append(value)
                    value = 1
                    repeat = True
                elif value == 0 and repeat == True:
                    row.append(value)
                    repeat = False
            pattern.append(row)

            if firstValue == 1:
                firstValue = 0
            else:
                firstValue = 1
        return pattern

    elif patternNumber == 7:
        #create a grid of alternating 11's and 00's starting with 11
        for i in range(0, len(grid)):
            row = []
            value = 1
            repeat = True
            for x in range(0, len(grid)):
                if value == 1 and repeat == False:
                    row.append(value)
                    value = 0
                    repeat = True
                elif value == 1 and repeat == True:
                    row.append(value)
                    repeat = False
                elif value == 0 and repeat == False:
                    row.append(value)
                    value = 1
                    repeat = True
                elif value == 0 and repeat == True:
                    row.append(value)
                    repeat = False
            pattern.append(row)

        return pattern


def nextPattern(patternNumber):
    #loops through all of the patterns
    global pattern

    randomFlag = True

    if randomFlag == True:
        r = list(range(0, 7+1))
        r.remove(patternNumber)
        patternNumber = random.choice(r)
    else:
        patternNumber += 1
        if patternNumber == 8:
            patternNumber = 0

    pattern = []
    print("Pattern No.: " + str(patternNumber))
    pattern = createPattern(patternNumber)
    printGrid(pattern)
    stripTracker(pattern)
    return patternNumber

#-----------------------------------------------------------#

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#setup for initial run

createGrid(size)
createTracker()
pattern = createPattern(patternSelection)
stripTracker(pattern)
printGrid(grid)

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(WINDOW_SIZE)

WIDTH = WINDOW_SIZE[0] / len(grid)
HEIGHT = WINDOW_SIZE[0] / len(grid)

# Set title of screen
pygame.display.set_caption("Grid Pattern")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#draw the grid once pygame is setup
drawGrid(grid)

#for use with rotation
degrees = 0

#Rotating Tracker
rotatingTracker = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if tracker != []:

        selectedRow = random.randint(0, len(tracker) - 1)
        selectedCell = random.randint(0,len(tracker[selectedRow]) - 1)

        contents = tracker[selectedRow].pop(selectedCell)
        grid[contents[0]][contents[1]] = pattern[contents[0]][contents[1]]
        #updateSquare(contents[0],contents[1])


        #----------------------
        #testing rotations - not working yet

        rotatingTracker.append([contents[0],contents[1],0, grid[contents[0]][contents[1]]])

        for index, square in enumerate(rotatingTracker):

            if square[3] == 1:

                img = pygame.image.load('curves_h.bmp')
                img = img.convert()
            else:
                img = pygame.image.load('curves_v.bmp')
                img = img.convert()

            img = pygame.transform.scale(img, (int(WIDTH), int(HEIGHT)))

            # rotate the image around 360 degrees but centralise it to x and y
            rotate_and_center(screen, int(HEIGHT * square[1]), int(HEIGHT * square[0]), img, square[2])

            # increment the rotation. reset rotation if degrees is greater than 359 (not necessary but cleaner IMO)
            if square[2] < 90:
                rotatingTracker[index][2] += 10
            else:
                del rotatingTracker[index]


        if len(tracker[selectedRow]) == 0:
            tracker.pop(selectedRow)
    else:
        #selects the next tracker
        createTracker()
        patternSelection = nextPattern(patternSelection)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
