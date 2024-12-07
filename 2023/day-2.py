from utils.FetchData import fetchData

useTestData = False
data = fetchData(2, 2023, useTestData)

maxRed = 12
maxGreen = 13
maxBlue = 14


def part1():
    total = 0
    for i, game in enumerate(data):
        valid = True
        rounds = [i.split(",") for i in game.split(":")[1].split(";")]
        for pick in rounds:
            for dice in pick:
                [amount, colour] = dice.strip().split(" ")
                if colour == "red":
                    if int(amount) > maxRed:
                        valid = False
                if colour == "green":
                    if int(amount) > maxGreen:
                        valid = False
                if colour == "blue":
                    if int(amount) > maxBlue:
                        valid = False
        if valid:
            total += i + 1

    print(total)


def part2():
    total = 0
    for i, game in enumerate(data):
        maxGreen = 0
        maxRed = 0
        maxBlue = 0
        rounds = [i.split(",") for i in game.split(":")[1].split(";")]
        for pick in rounds:
            for dice in pick:
                [amount, colour] = dice.strip().split(" ")
                if colour == "red":
                    if int(amount) > maxRed:
                        maxRed = int(amount)
                if colour == "green":
                    if int(amount) > maxGreen:
                        maxGreen = int(amount)
                if colour == "blue":
                    if int(amount) > maxBlue:
                        maxBlue = int(amount)
        total += maxGreen * maxBlue * maxRed
    print(total)


# part1()
part2()
# 56314
