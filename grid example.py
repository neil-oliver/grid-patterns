#20x20 grid
import random

grid = []
tracker = []

def printGrid(grid):
    #pretty printing of grid
    for row in grid:
        print(row)
    print("\n")
        

def create(size):
    #create grid of a given size with random 1's & 0's
    global grid
    for i in range(size):
        row = []
        for x in range(size):
            row.append(random.randrange(2))
        grid.append(row)
    printGrid(grid)


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
        printGrid(tracker)


def createPattern(patternNumber):
    #create a grid with a set pattern
    global grid

    if patternNumber == 0:
        # create a grid of all 0's
        pattern = []
        for i in range(0,len(grid)):
            row = []
            for x in range(0,len(grid)):
                row.append(0)
            pattern.append(row)
        return pattern

    elif patternNumber == 1:
            # create a grid of all 1's
            pattern = []
            for i in range(0, len(grid)):
                row = []
                for x in range(0, len(grid)):
                    row.append(1)
                pattern.append(row)
            return pattern


def randomReplace():
    #randomly replace elements until a pattern has been achieved
    global grid
    global tracker

    createTracker()
    pattern = createPattern(0)
    printGrid(pattern)
    stripTracker(pattern)


    while tracker != []:

        selectedRow = random.randint(0, len(tracker) - 1)
        selectedCell = random.randint(0,len(tracker[selectedRow]) - 1)

        contents = tracker[selectedRow].pop(selectedCell)
        grid[contents[0]][contents[1]] = 1 #this is where it will replace according to a pattern
        printGrid(grid)

        if len(tracker[selectedRow]) == 0:
            tracker.pop(selectedRow)



#-----------------------------------------------------------#

size = int(input("please enter a size between 5 & 50: \n"))
if size >= 5 and size <= 50:
    create(size)
    randomReplace()
else:
    print("incorrect size entered")


