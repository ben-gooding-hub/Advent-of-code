from utils.FetchData import fetchData

useTestData = False
data = fetchData(1, 2023, useTestData)


def part1():
    total = 0
    for input in data:
        parsedInput = ""
        for char in input:
            if char.isnumeric():
                parsedInput += char
        total += int(parsedInput[0] + parsedInput[-1])
    print(total)


def part2():
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    maxNumberLength = len(max(numbers, key=len))
    minNumberLength = len(min(numbers, key=len))
    total = 0
    for input in data:
        # Find all indexes of potential numbers and sort them
        numberIndexes = []
        for key, val in numbers.items():
            [numberIndexes.append(i) for i in findAllOccurrences(input, key)]
            [numberIndexes.append(i) for i in findAllOccurrences(input, str(val))]
        numberIndexes.sort()

        # Get the first and last potential number (string or int)
        firstNumber = None
        for i in range(minNumberLength, maxNumberLength + 1):
            for key, val in numbers.items():
                if input[numberIndexes[0]:numberIndexes[0] + i] == key:
                    firstNumber = val
                    break
        if not firstNumber:
            firstNumber = int(input[numberIndexes[0]])

        secondNumber = None
        for i in range(minNumberLength, maxNumberLength + 1):
            for key, val in numbers.items():
                if input[numberIndexes[-1]:numberIndexes[-1] + i] == key:
                    secondNumber = val
        if not secondNumber:
            secondNumber = int(input[numberIndexes[-1]])

        calcVal = int(str(firstNumber) + str(secondNumber))
        total += calcVal
    print(total)


def findAllOccurrences(string, substring):
    return [i for i in range(len(string)) if string.startswith(substring, i)]


# part1()
part2()
# 56314
