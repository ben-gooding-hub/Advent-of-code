from utils.FetchData import fetchData

useTestData = True
data = fetchData(9, 2024, useTestData)

numberCount = 0
disk = ""
for key, char in data:
    if key % 2 == 0:
        disk += "." * int(char)
    else
        disk += f"{char}" * int(char)