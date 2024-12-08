import re

from utils.FetchData import fetchData
from utils.Timer import timeMethod

useTestData = False
data = fetchData(7, 2024, useTestData)
parsedData: list[tuple[int, list[int]]] = [(int(x), [int(strY) for strY in y.strip().split()]) for (x, y) in [re.match(r"(\d+):(.*)", line).groups() for line in data]]

def performOperation(operator: str, num1: int, num2: int) -> int:
    if operator == "+":
        return num1 + num2
    if operator == "*":
        return num1 * num2
    if operator == "||":
        return int(str(num1) + str(num2))
    raise Exception("Invalid operator")

def recursiveOperateOnNext(lastTotal: int, currentList: list[int], totalToFind: int, operators: list[str]) -> (int, bool):
    # Optimise
    if lastTotal > totalToFind:
        return None, False

    # Handle final case
    if len(currentList) == 0:
        if lastTotal == totalToFind:
            return totalToFind, True
        else:
            return None, False

    # Handle n -> n+1 step
    for operator in operators:
        operatorAttempt = performOperation(operator, lastTotal, currentList[0])
        (totalFound, solutionWasFound) = recursiveOperateOnNext(operatorAttempt, currentList[1:], totalToFind, operators)
        if solutionWasFound:
            return (totalFound, solutionWasFound)

    # No more possible solutions exit
    return None, False

def sumValidCalibrations(data: list[tuple[int, list[int]]], operators: list[str]):
    total = 0
    for (totalToFind, values) in data:
        (totalFound, solutionWasFound) = recursiveOperateOnNext(values[0], values[1:], totalToFind, operators)
        if solutionWasFound:
            total += totalFound
    print(total)


timeMethod(lambda: sumValidCalibrations(parsedData, ["+", "*"]))

timeMethod(lambda: sumValidCalibrations(parsedData, ["+", "*", "||"]))

