import re

##define count
def get_TreeCount (inputList, xStep, yStep, geoCount):
    treeCount = 0
    xCoord = 0
    yCoord = 0
        
    for i in range(0,len(inputList),yStep):
        treeTest = inputList[yCoord][xCoord % geoCount]
        if treeTest == "#":
            treeCount += 1
        yCoord += yStep
        xCoord += xStep
    return treeCount


##Open inputs and parse
with open("input.txt", "r") as f:
	   inputList = f.read()
	   inputList = inputList.split("\n")

geoCount = len(inputList[0])

##Part 1
treeCount = get_TreeCount(inputList, 3, 1, geoCount)
print (treeCount)

##Part 2
slopes = [
            [1,1],
            [3,1],
            [5,1],
            [7,1],
            [1,2]
          ]
treeCount = 1      
for tests in slopes:
    treeCount = treeCount * get_TreeCount(inputList,tests[0],tests[1],geoCount)

print(treeCount)
