from typing import Optional

from utils.TupleTools import addTuples


def isInBounds(position: tuple[int, int], xYMax: tuple[int, int]) -> bool:
    return 0 <= position[0] < xYMax[0] and 0 <= position[1] < xYMax[1]

def getChar(x: int, y: int, data: list[str], xYMax: tuple[int, int]) -> Optional[str]:
    if not isInBounds((x, y), xYMax):
        return None
    return data[y][x]

def getCharTuple(position: tuple[int, int], data: list[str], xYMax: tuple[int, int]) -> Optional[str]:
    if not isInBounds(position, xYMax):
        return None
    return data[position[1]][position[0]]

neighbourVectors = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

def getNeighbours(position: tuple[int, int], data: list[str], xyMax: tuple[int, int]) -> list[tuple[int, int]]:
    neighbours = []
    for neighbourVector in neighbourVectors:
        neighbour = addTuples(position, neighbourVector)
        if getCharTuple(neighbour, data, xyMax):
            neighbours.append(neighbour)
    return neighbours

def getNeighboursIncludingOutOfBounds(position: tuple[int, int], data: list[str], xyMax: tuple[int, int]) -> list[Optional[tuple[int, int]]]:
    neighbours = []
    for neighbourVector in neighbourVectors:
        neighbour = addTuples(position, neighbourVector)
        if getCharTuple(neighbour, data, xyMax):
            neighbours.append(neighbour)
        else:
            neighbours.append(None)
    return neighbours

def findGroupsOfChar(position: tuple[int, int], data: list[str], xyMax: tuple[int, int]) -> set[tuple[int, int]]:
    group = set()
    checkPositions: list[tuple[int, int]] = [position]
    groupChar = getCharTuple(position, data, xyMax)
    while len(checkPositions) > 0:
        positionToCheck = checkPositions[0]
        for neighbour in getNeighbours(positionToCheck, data, xyMax):
            if getCharTuple(neighbour, data, xyMax) == groupChar:
                if neighbour not in group and neighbour not in checkPositions:
                    checkPositions.append(neighbour)
        del checkPositions[0]
        group.add(positionToCheck)
    return group