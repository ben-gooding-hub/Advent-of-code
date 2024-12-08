from utils.FetchData import fetchData
from utils.TwoDimGridTools import isInBounds

useTestData = False
data = fetchData(8, 2024, useTestData)

def addCoordsToNodeTracker(nodeTracker: dict[str, list[tuple[int, int]]], newChar: str, coords: tuple[int, int]):
    nodeList = nodeTracker.get(newChar)
    if nodeList == None:
        nodeTracker[newChar] = [coords]
    else:
        nodeList.append(coords)

def calculateAntiNodesForPair(first: tuple[int, int], second: tuple[int, int], xMax: int, yMax: int) -> set[tuple[int, int]]:
    xDiff = first[0] - second[0]
    yDiff = first[1] - second[1]
    nodeResult = set()
    nodeOne = (first[0] + xDiff, first[1] + yDiff)
    nodeTwo = (second[0] - xDiff, second[1] - yDiff)
    if isInBounds(nodeOne,(xMax, yMax)):
        nodeResult.add(nodeOne)
    if isInBounds(nodeTwo,(xMax, yMax)):
        nodeResult.add(nodeTwo)
    return nodeResult

def calculateAntiNodesForPairRepeated(first: tuple[int, int], second: tuple[int, int], xMax: int, yMax: int) -> set[tuple[int, int]]:
    xDiff = first[0] - second[0]
    yDiff = first[1] - second[1]
    nodeResult = set()
    potentialAntiNode = first
    while isInBounds(potentialAntiNode,(xMax, yMax)):
        nodeResult.add(potentialAntiNode)
        potentialAntiNode = potentialAntiNode[0] + xDiff, potentialAntiNode[1] + yDiff
    potentialAntiNode = first
    while isInBounds(potentialAntiNode,(xMax, yMax)):
        nodeResult.add(potentialAntiNode)
        potentialAntiNode = potentialAntiNode[0] - xDiff, potentialAntiNode[1] - yDiff

    return nodeResult

xMax = len(data[0])
yMax = len(data)
nodeTracker: dict[str, list[tuple[int, int]]] = {}
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == ".":
            continue
        addCoordsToNodeTracker(nodeTracker, char, (x, y))

antiNodes = set[(int, int)]()
for nodeList in nodeTracker.values():
    for nodeKey, node in enumerate(nodeList):
        for existingNode in nodeList[0:nodeKey]:
            for antiNode in calculateAntiNodesForPair(node, existingNode, xMax, yMax):
                antiNodes.add(antiNode)
print(len(antiNodes))

antiNodes = set[(int, int)]()
for nodeList in nodeTracker.values():
    for nodeKey, node in enumerate(nodeList):
        for existingNode in nodeList[0:nodeKey]:
            for antiNode in calculateAntiNodesForPairRepeated(node, existingNode, xMax, yMax):
                antiNodes.add(antiNode)
print(len(antiNodes))
