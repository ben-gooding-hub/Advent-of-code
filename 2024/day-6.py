from utils.FetchData import fetchData
from utils.TwoDimGridTools import isInBounds, getCharTuple
from time import time

useTestData = False
data = fetchData(6, 2024, useTestData)

def findStart(data: list[str]) -> tuple[int, int]:
    for y, line in enumerate(data):
        for x, cell in enumerate(line):
            if cell == "^":
                return x, y
    raise Exception("No start point")

start = findStart(data)

yMax = len(data)
xMax = len(data[0])


def isHash(x: int, y: int, data: list[str]) -> bool:
    return getCharTuple((x, y), data, (xMax, yMax)) == "#"

def getNextDirection(currentDirection: tuple[int, int]) -> tuple[int, int]:
    directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]
    return directions[(directions.index(currentDirection) + 1) % 4]


def addTuple(first: tuple[int, int], second: tuple[int, int]):
    return first[0] + second[0], first[1] + second[1]


currentDirection = (0, -1)
currentLocation = start

def walkForward(currentLocation: tuple[int, int], currentDirection: tuple[int, int], data: list[str]) -> tuple[
    tuple[int, int], tuple[int, int]]:
    localDirection = currentDirection
    turnCount = 0
    while turnCount < 5:
        potentialNewSpot = addTuple(currentLocation, localDirection)
        if isHash(potentialNewSpot[0], potentialNewSpot[1], data):
            localDirection = getNextDirection(localDirection)
            turnCount += 1
        else:
            return potentialNewSpot, localDirection
    raise Exception("Stuck")


walkedSpots = set[int, int]()
while isInBounds(currentLocation):
    walkedSpots.add(currentLocation)
    currentLocation, currentDirection = walkForward(currentLocation, currentDirection, data)

print(len(walkedSpots))

def potentialNewObstructionData(data: list[str], obstructionTrailSpot: tuple[int, int]) -> list[str]:
    newData = data.copy()
    temp = list(newData[obstructionTrailSpot[1]])
    temp[obstructionTrailSpot[0]] = "#"
    newData[obstructionTrailSpot[1]] = ''.join(temp)
    return newData

def isTrailValid(data: list[str])-> bool:
    currentLocation = start
    currentDirection = (0, -1)
    walkedSpotsWithDir: set = set[tuple[int, int], tuple[int, int]]()
    while isInBounds(currentLocation):
        walkedSpotsWithDir.add((currentLocation, currentDirection))
        currentLocation, currentDirection = walkForward(currentLocation, currentDirection, data)
        if (currentLocation, currentDirection) in walkedSpotsWithDir:
            return False
    return True


t0 = time()

count = 0
obstructionSpots = set[int, int]()
for obstructionTrailSpot in walkedSpots:
    newData = potentialNewObstructionData(data, obstructionTrailSpot)
    if not isTrailValid(newData):
        count += 1


t1 = time()
print(count)
print(f"done in {t1 - t0}")

