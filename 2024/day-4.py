from utils.FetchData import fetchData
from typing import Optional
from utils.TwoDimGridTools import getChar

useTestData = False
data = fetchData(4, 2024, useTestData)

yMax = len(data)
xMax = len(data[0])

def getCharAt(x: int, y: int) -> Optional[str]:
    return getChar(x, y, data,(xMax, yMax))

def findPotentialDirectionOfSecondLetter(x: int, y: int, secondLetter: str) -> list[tuple[int, int]]:
    potentialDirection: list[tuple[int, int]] = []
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0,  -1),          (0,  1),
        (1,  -1), (1,  0), (1,  1)
    ]
    for (xDir, yDir) in directions:
        if getCharAt(x + xDir, y + yDir) == secondLetter:
            potentialDirection.append((xDir, yDir))
    return potentialDirection

count = 0
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "X":
            for maybeXmasDir in findPotentialDirectionOfSecondLetter(x, y, secondLetter="M"):
                if getCharAt(x + maybeXmasDir[0] * 2, y + maybeXmasDir[1] * 2) == "A":
                    if getCharAt(x + maybeXmasDir[0] * 3, y + maybeXmasDir[1] * 3) == "S":
                        count += 1

print(count)

count = 0
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "A":
            if getCharAt(x -1, y - 1) == "M":
                if getCharAt(x + 1, y - 1) == "S":
                    if getCharAt(x + -1, y +1) == "M":
                        if getCharAt(x + 1, y +1) == "S":
                            count += 1
            if getCharAt(x - 1, y - 1) == "M":
                if getCharAt(x + 1, y - 1) == "M":
                    if getCharAt(x + -1, y + 1) == "S":
                        if getCharAt(x + 1, y + 1) == "S":
                            count += 1
            if getCharAt(x - 1, y - 1) == "S":
                if getCharAt(x + 1, y - 1) == "S":
                    if getCharAt(x + -1, y + 1) == "M":
                        if getCharAt(x + 1, y + 1) == "M":
                            count += 1
            if getCharAt(x - 1, y - 1) == "S":
                if getCharAt(x + 1, y - 1) == "M":
                    if getCharAt(x + -1, y + 1) == "S":
                        if getCharAt(x + 1, y + 1) == "M":
                            count += 1

print(count)