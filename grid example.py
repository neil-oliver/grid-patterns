#20x20 grid
import random

grid = []

def create(size):
    global grid
    for i in range(size):
        row = []
        for x in range(size):
            row.append(random.randrange(2))
        grid.append(row)

    print(grid)

def randEachCell():
    #loop through each value and regenerate a value
    for rowindex, row in enumerate(grid):
        for cellindex, cellvalue in enumerate(row):
            row[cellindex] = random.randrange(2)
            print(grid)


size = int(input("please enter your size: \n"))
create(size)
randEachCell()

