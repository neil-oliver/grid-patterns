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
    pattern = []
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
        for i in range(0, len(grid)):
            row = []
            for x in range(0, len(grid)):
                if value == 1:
                    row.append(value)
                    value = 0
                else:
                    row.append(value)
                    value = 1
            pattern.append(row)
        return pattern

    elif patternNumber == 3:
        #create a grid of alternating 1's and 0's starting on same number
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

def nextPattern(patternNumber):
    for repeat in range(1,4):
        print("Running Next Pattern")
        if patternNumber == 4:
            randomReplace(0)
            patternNumber += 1
        else:
            patternNumber += 1
            randomReplace(patternNumber)

def randomReplace(patternNumber):
    #randomly replace elements until a pattern has been achieved
    global grid
    global tracker

    createTracker()
    pattern = createPattern(patternNumber)
    stripTracker(pattern)
    printGrid(grid)

    while tracker != []:

        selectedRow = random.randint(0, len(tracker) - 1)
        selectedCell = random.randint(0,len(tracker[selectedRow]) - 1)

        contents = tracker[selectedRow].pop(selectedCell)
        grid[contents[0]][contents[1]] = pattern[contents[0]][contents[1]]
        printGrid(grid)

        if len(tracker[selectedRow]) == 0:
            tracker.pop(selectedRow)

    print("*** Pattern Achieved *** \n")

#-----------------------------------------------------------#

size = int(input("please enter a size between 5 & 50: \n"))
if size >= 5 and size <= 50:
    create(size)
    pattern = int(input("please select a pattern from the following list: \n 0. All 00000's \n 1. All 11111's \n 2. Alternating 101010 \n 3. Alternating 101010 same each line \n 4. Alternating lines of 1's and 0's \n"))

    if pattern >= 0 and pattern <= 4:
        print("Starting with a " + str(size) + " X " + str(size) + " grid.")
        print("Modifying values to achieve pattern... \n")
        randomReplace(pattern)
    else:
        print("incorrect menu selection entered")
else:
    print("incorrect size entered")

nextPattern(pattern + 1)




