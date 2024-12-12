from utils.FetchData import fetchData
from utils.TupleTools import addTuples
from utils.TwoDimGridTools import isInBounds, getChar

useTestData = False
data = fetchData(10, 2024, useTestData)

print(data)
xyMax = len(data[0]), len(data)

trailheads: list[tuple[int, int]] = []
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if cell == "0":
            trailheads.append((x,y))

def findStepsHigher(currentSpot: tuple[int, int]) -> list[tuple[int, int]]:
    potentialDirections = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    nextSteps = []
    currentValue = getChar(currentSpot[0], currentSpot[1], data, xyMax)
    for direction in potentialDirections:
        potentialNewSpot = addTuples(direction, currentSpot)
        newSpotValue = getChar(potentialNewSpot[0], potentialNewSpot[1], data, xyMax)
        if newSpotValue is None:
            continue
        if int(newSpotValue) == int(currentValue) + 1:
            nextSteps.append(potentialNewSpot)
    return nextSteps

cache = {}
def addSpotToCache(spot: tuple[int, int], value: int):
    cache[spot] = value
def resetCache():
    cache = {}

def findRoutesToTheTopFromSpot(spot: tuple[int, int]) -> int:
    if spot in cache:
        return cache[spot]
    currentValue = int(getChar(spot[0], spot[1], data, xyMax))

    if currentValue == 9:
        addSpotToCache(spot, 1)
        return 1
    else:
        spotCount = 0

        for nextStep in findStepsHigher(spot):
            spotValue = findRoutesToTheTopFromSpot(nextStep)
            addSpotToCache(nextStep, spotValue)
            spotCount += spotValue

        addSpotToCache(spot, spotCount)
        return spotCount

def findTrailHeadScore(trailhead: tuple[int, int]) -> int:
    return findRoutesToTheTopFromSpot(trailhead)

score = 0
# print(trailheads)
for trailhead in trailheads:
    score += findTrailHeadScore(trailhead)
for line in data:
    # print(line)
    pass
print(score)