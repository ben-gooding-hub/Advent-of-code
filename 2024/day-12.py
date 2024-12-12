from utils.FetchData import fetchData
from utils.TupleTools import subtractTuples
from utils.TwoDimGridTools import getNeighbours, getNeighboursIncludingOutOfBounds, findGroupsOfChar, getCharTuple

useTestData = False
data = fetchData(12, 2024, useTestData)

print(data)
xyMax = (len(data[0]), len(data))

def calculatePerimeter(plotLocations: set[tuple[int, int]], plotType: str) -> int:
    count = 0
    for plotLocation in plotLocations:
        neighbourChars = [getCharTuple(pos, data, xyMax) for pos in getNeighbours(plotLocation, data, xyMax)]
        realNeighbours = [char for char in neighbourChars if char == plotType]
        count += (4 - len(realNeighbours))
    return count

def findFencesForPositionInPlot(position: tuple[int, int]) -> list[tuple[int, int]]:
    plotType = getCharTuple(position,data,xyMax)
    neighbours = getNeighbours(position, data, xyMax)
    realNeighbours = [pos for pos in neighbours if getCharTuple(pos, data, xyMax) == plotType]
    neighbourUnitVectors = []
    for neighbour in realNeighbours:
        neighbourUnitVectors.append(subtractTuples(neighbour, position))
    return neighbourUnitVectors


groups = []

for y, row in enumerate(data):
    for x, cell in enumerate(row):
        alreadyInGroup = False
        for group in groups:
            if (x, y) in group:
                alreadyInGroup = True
                break
        if not alreadyInGroup:
            groups.append(findGroupsOfChar((x, y), data, xyMax))

count = 0
for group in groups:
    for firstChar in group:
        break
    count += (calculatePerimeter(group, getCharTuple(firstChar, data, xyMax)) * len(group))

for group in groups:
    fencePositions = {}
    for spot in group:
        fenceUnitVectors = findFencesForPositionInPlot(spot)
        fencePositions[spot] = fenceUnitVectors
    for firstPlot in group:
        if firstPlot in fencePositions:
            break
    firstFence = fencePositions[firstPlot]
    currentFence = firstFence
    currentPlot = firstPlot
    fenceCount = 1
    usedAlready = set()
    plotType = getCharTuple(firstPlot,data,xyMax)
    while True:
        for fence in fencePositions[currentPlot]:
            if (currentFence, fence) not in usedAlready:
                usedAlready.add((currentFence, fence))
        neighbours = getNeighbours(firstPlot, data, xyMax)
        realNeighbours = [pos for pos in neighbours if getCharTuple(pos, data, xyMax) == plotType]

        for neighbour in realNeighbours:
            fencePositions[neighbour]

        if nextFence == firstFence:
            break


print(count)
