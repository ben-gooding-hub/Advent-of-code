from math import floor

from utils.FetchData import fetchData

useTestData = False
data = fetchData(9, 2024, useTestData)[0]
# data = "151010"
numberCount = 0
disk = []
for key, char in enumerate(data):
    if key % 2 == 0:
        num = floor((key + 1)/2)
        disk += f"{num}" * int(char)
        # for i in range(int(char)):
        #     disk.append(f"{num}")
    else:
        disk += "." * int(char)
# print(disk)
# disk = list("00...111...2...333.44.5558.1.777.888899")
dotKeys = [key for key, char in enumerate(disk) if char == "."]
# print(dotKeys)
dotCount = len(dotKeys)
dupeKeys = 0
for key, dot in enumerate(dotKeys):
    if disk[-key - 1] == ".":
        dupeKeys += 1

# for i in range(dotCount + dupeKeys):

# print(dupeKeys)

moveStrs = [(key,char) for key, char in enumerate(disk) if char != "."]
moveStrs.reverse()
print("here",max(moveStrs))
# print("".join(moveStrs))

for i in range(dotCount - dupeKeys):
    # print(moveStrs[i])
    disk[dotKeys[i]] = moveStrs[i][1]
    # while(disk[-1] == "."):
    #     del disk[-1]
    disk[moveStrs[i][0]] = "."
    # del disk[-1]
    # while(disk[-1] == "."):
    #     del disk[-1]
    # print("".join(disk))
    # print(-key - 1)
    # disk[-key - 1] = "."
# print("".join(disk))
finalStrWithoutPadding = disk
# print("".join(finalStrWithoutPadding))
checksum = 0
length = len(finalStrWithoutPadding)
for key, num in enumerate(finalStrWithoutPadding):
    if num == ".":
        continue
    # print(finalStrWithoutPadding[key:key+10], key, num, length)
    checksum += key * int(num)
print(checksum)
# for num
# 0099811188827773336446555566
# 0099811188827773336446555566
# 00...111...2...333.44.5555.6666.777.888899
# 00...111...2...333.44.5555.6666.777.888899

# 91380424522 too low
# 91380424522 too low

# 00...111...2...333.44.5555.6666.777.888899
# 009..111...2...333.44.5555.6666.777.88889.
# 0099.111...2...333.44.5555.6666.777.8888..
# 00998111...2...333.44.5555.6666.777.888...
# 009981118..2...333.44.5555.6666.777.88....
# 0099811188.2...333.44.5555.6666.777.8.....
# 009981118882...333.44.5555.6666.777.......
# 0099811188827..333.44.5555.6666.77........
# 00998111888277.333.44.5555.6666.7.........
# 009981118882777333.44.5555.6666...........
# 009981118882777333644.5555.666............
# 00998111888277733364465555.66.............
# 0099811188827773336446555566..............

# 00...111...2...333.44.5555.6666.777.888899
# 009..111...2...333.44.5555.6666.777.88889.
# 0099.111...2...333.44.5555.6666.777.8888..
# 00998111...2...333.44.5555.6666.777.888...
# 009981118..2...333.44.5555.6666.777.88....
# 0099811188.2...333.44.5555.6666.777.8.....
# 009981118882...333.44.5555.6666.777.......
# 0099811188827..333.44.5555.6666.77........
# 00998111888277.333.44.5555.6666.7.........
# 009981118882777333.44.5555.6666...........
# 009981118882777333644.5555.666............
# 00998111888277733364465555.66.............
# 0099811188827773336446555566..............
