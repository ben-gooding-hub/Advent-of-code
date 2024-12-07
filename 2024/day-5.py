from utils.FetchData import fetchData
from math import floor

useTestData = False
data = fetchData(5, 2024, useTestData)

# print(data)

# This assumes x and y are in the page
def checkXisBeforeY(x, y, page) -> bool:
    for num in page:
        if num == x:
            return True
        if num == y:
            return False
    raise Exception("Invalid usage, x and y must be in page")

def middlePageNumber(page) -> int:
    return page[floor(len(page) / 2)]

def fixPageOrderingAndReturnMiddle(page: list[int], pageOrderingRules: list[tuple[int, int]]) -> int:
    needsRestarting = True
    while needsRestarting:
        for (x, y) in pageOrderingRules:
            if x in page and y in page:
                if not checkXisBeforeY(x, y, page):
                    # Swap x and y
                    xIndex, yIndex = page.index(x), page.index(y)
                    page[xIndex], page[yIndex] = page[yIndex], page[xIndex]
                    break
        else:
            needsRestarting = False
    return middlePageNumber(page)

splitKey = 0
for key, item in enumerate(data):
    if item == "":
        splitKey = key
        break

# Parse data
pageOrderingRules: list[tuple[int, int]] = [tuple([int(ruleVal) for ruleVal in ruleString.split("|")]) for ruleString in data[0:splitKey]]
pagesToProduce: list[list[int]] = [[int(item) for item in page.split(",")] for page in data[splitKey+1:]]

totalPartOne = 0
totalPartTwo = 0

for page in pagesToProduce:
    for (x, y) in pageOrderingRules:
        if x in page and y in page:
            if not checkXisBeforeY(x, y, page):
                # Found Issue - calc part 2 and then skip the rest of the rules
                totalPartTwo += fixPageOrderingAndReturnMiddle(page, pageOrderingRules)
                break
    else:
        # No problems found
        totalPartOne += middlePageNumber(page)

print(totalPartOne)
print(totalPartTwo)