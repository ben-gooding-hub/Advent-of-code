import re
from utils.FetchData import fetchData

useTestData = False
data = fetchData(3, 2024, useTestData)
data = "".join(data)

def mul(mulString):
    first = re.search(r"\(\d+", mulString).group()[1:]
    second = re.search(r",\d+", mulString).group()[1:]
    if len(first) > 3 or len(second) > 3:
        return 0
    return int(first) * int(second)

res = re.findall(r"mul\(\d+,\d+\)", data)
total = 0

for captured in res:
    total += mul(captured)

print(total)

# f = open("example-data/3-part2", "r")
f = open("data/3", "r")
data = f"do(){f.read()}don't()"
f.close()

res = re.findall(r"do\(\)(.*?)don't\(\)", data, flags=re.DOTALL)

total = 0
for captured in res:
    res2 = re.findall(r"mul\(\d+,\d+\)", captured)
    for captured2 in res2:
        total += mul(captured2)

print(total)


