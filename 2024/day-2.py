f = open("example-data/2", "r")
# f = open("data/2", "r")
data = f.read().split("\n")
# print(data)
f.close()

total = 0

def isSafe(nums: list[int]):
    lastNumber = -100
    goingUp = -100
    safe = True
    for num in nums:
        if lastNumber == -100:
            pass
        else:
            if goingUp == -100:
                goingUp = num > lastNumber
            if abs(num - lastNumber) > 3 or abs(num - lastNumber) == 0:
                safe = False
            if goingUp and num < lastNumber:
                safe = False
            if not goingUp and num > lastNumber:
                safe = False
        lastNumber = num
    return safe

for line in data:

    items = [int(x) for x in line.split()]
    if isSafe(items):
        total += 1
        continue
    for index, i in enumerate(items):

        items2 = items.copy()
        del items2[index]
        print(items2)
        if isSafe(items2):
            print("safe",items2)
            total += 1
            break





print(total)