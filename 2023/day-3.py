from utils.FetchData import fetchData

useTestData = False
data = fetchData(3, 2023, useTestData)


def isSymbol(char):
    return char not in "0123456789."


def isValidNumber(data, colIndex, rowIndex, numbersLength, maxRow, maxCol):
    for rowIndexCheck in range(rowIndex - 1, rowIndex + 2):
        if rowIndexCheck < 0 or rowIndexCheck >= maxRow:
            continue
        for colIndexCheck in range(colIndex - 1, colIndex + numbersLength + 1):
            if colIndexCheck < 0 or colIndexCheck >= maxCol:
                continue
            if isSymbol(data[rowIndexCheck][colIndexCheck]):
                # pass
                return True
    return False


def part1():
    total = 0
    colLength = len(data[0])
    colMaxIndex = len(data[0]) - 1
    rowLength = len(data)
    for rowIndex, row in enumerate(data):

        colIndex = 0
        while colIndex <= colMaxIndex:
            if not row[colIndex].isdigit():
                colIndex += 1
                continue
            initialColIndex = colIndex
            numbersLength = 1
            colIndex += 1
            while colIndex <= colMaxIndex and row[colIndex].isdigit():
                numbersLength += 1
                colIndex += 1
            if isValidNumber(data, initialColIndex, rowIndex, numbersLength, rowLength, colLength):
                total += int(row[initialColIndex:initialColIndex + numbersLength])
    print(total)


part1()
# part2()
