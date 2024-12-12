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
def addSpotToCache(spot: tuple[int, int], acc: set[tuple[int, int]]):
    cache[spot] = acc
def resetCache():
    cache = {}

def findRoutesToTheTopFromSpot(spot: tuple[int, int], acc: set[tuple[int, int]]) -> set[tuple[int, int]]:
    thisAcc = acc.copy()
    if spot in cache:
        return cache[spot]
    currentValue = int(getChar(spot[0], spot[1], data, xyMax))
    if currentValue == 9:
        thisAcc.add(spot)
        addSpotToCache(spot, thisAcc)
        return thisAcc
    else:

        copyAgain = thisAcc.copy()
        for nextStep in findStepsHigher(spot):
            spotValue = findRoutesToTheTopFromSpot(nextStep, thisAcc)
            copyAgain = copyAgain.union(spotValue)
            addSpotToCache(nextStep, spotValue)

        addSpotToCache(spot, copyAgain)
        return copyAgain

def findTrailHeadScore(trailhead: tuple[int, int]) -> int:
    return len(findRoutesToTheTopFromSpot(trailhead, set()))


score = 0
# print(trailheads)
for trailhead in trailheads:
    score += findTrailHeadScore(trailhead)
    resetCache()
for line in data:
    # print(line)
    pass
print(score)