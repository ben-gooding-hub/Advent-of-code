from utils.FetchData import fetchData

useTestData = False
data = fetchData(11, 2024, useTestData)

cache = {}
def addToCache(num: int, res: list[int]):
    cache[num] = res

def applyRule(engraving: int) -> list[int]:
    if engraving == 0:
        return [1]
    digits = len(str(engraving))
    if digits % 2 == 0:
        strNum = str(engraving)
        halfway = int(digits/2)
        return [int(strNum[0:halfway]), int(strNum[halfway:])]
    return [engraving * 2024]

def applyWithCache(engraving: int) -> list[int]:
    if engraving in cache:
         return cache[engraving]
    else:
        appliedRule = applyRule(engraving)
        addToCache(engraving, appliedRule)
        return appliedRule

def blink(engravings: dict[int, int]) -> dict[int, int]:
    newEngravings: dict[int, int] = {}
    for engraving, count in engravings.items():
        newOnes = multiplyDictCount(collectDuplicateEngravingsWithCount(applyWithCache(engraving)), count)
        newEngravings = mergeDicts(newOnes, newEngravings)
    return newEngravings

def multiplyDictCount(app: dict[int, int], multiple: int) -> dict[int, int]:
    for key, _ in app.items():
        app[key] *= multiple
    return app

def mergeDicts(first: dict[int, int], second: dict[int, int]) -> dict[int, int]:
    for key, val in first.items():
        if key in second:
            second[key] += val
        else:
            second[key] = val
    return second

def collectDuplicateEngravingsWithCount(engravings: list[int]) -> dict[int, int]:
    engravingsFound = {}
    for engraving in engravings:
        if engraving in engravingsFound:
            engravingsFound[engraving] += 1
        else:
            engravingsFound[engraving] = 1
    return engravingsFound

initialEngravings = collectDuplicateEngravingsWithCount([int(string) for string in data[0].split()])

blinkCount = 1000
currentEngravings = initialEngravings
for i in range(blinkCount):
    currentEngravings = blink(currentEngravings)

print(sum(currentEngravings.values()))

# x -> y -> x, z
# x after 2 blinks returns x,z
# f(x, 2) = x, z
# after 4 blinks -> x, z, f(z, 2)
# after 6 blinks -> x, z, f(z, 2), f(z, 4)
# after 8 blinks -> x, z, f(z, 2), f(z, 4), f(z, 6)

# f(x, 2) = f(x, 0) + z
# f(x, 4) = f(x, 2) + f(z, 2)
# f(x, 6) = f(x, 4) + f(z, 4)
# to perform 2 blinks N = N + f(x, 2)

