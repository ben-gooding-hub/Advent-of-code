# data = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3""".splitlines()
f = open("data/1", "r")
data = f.read().split("\n")
print(data)
f.close()


leftList = []
rightList = []

for line in data:
    temp = line.split()
    leftList.append(int(temp[0]))
    rightList.append(int(temp[-1]))

rightList.sort()
leftList.sort()
total = 0
for key, i in enumerate(data):

    total += abs(rightList[key] - leftList[key])

print(total)

dic = {}
lastFound = 0
for i in leftList:
    if i == lastFound:
        count = dic[lastFound]
        dic[lastFound] = count + 1
        continue
    else:
        lastFound = i
        dic[lastFound] = 1

total = 0
for key, val in dic.items():
    count = 0
    for i in rightList:
        if key == i:
            count += 1
    total += count * val * key

print(total)
