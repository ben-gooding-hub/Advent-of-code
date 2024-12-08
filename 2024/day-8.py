from utils.FetchData import fetchData
from utils.TupleTools import subtractTuples, addTuples
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
    vectorDiff = subtractTuples(first, second)
    nodeOne = addTuples(first, vectorDiff)
    nodeTwo = subtractTuples(second, vectorDiff)
    nodeResult = set()
    if isInBounds(nodeOne,(xMax, yMax)):
        nodeResult.add(nodeOne)
    if isInBounds(nodeTwo,(xMax, yMax)):
        nodeResult.add(nodeTwo)
    return nodeResult

def calculateAntiNodesForPairRepeated(first: tuple[int, int], second: tuple[int, int], xMax: int, yMax: int) -> set[tuple[int, int]]:
    vectorDiff = subtractTuples(first, second)
    nodeResult = set()

    potentialAntiNode = first
    while isInBounds(potentialAntiNode,(xMax, yMax)):
        nodeResult.add(potentialAntiNode)
        potentialAntiNode = addTuples(potentialAntiNode, vectorDiff)

    potentialAntiNode = first
    while isInBounds(potentialAntiNode,(xMax, yMax)):
        nodeResult.add(potentialAntiNode)
        potentialAntiNode = subtractTuples(potentialAntiNode, vectorDiff)

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
