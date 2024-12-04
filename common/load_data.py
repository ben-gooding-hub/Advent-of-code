def loadData(day: int, isExampleData: bool = False) -> list[str]:
    folder = "example-data" if isExampleData else "data"
    f = open(f"{folder}/{str(day)}", "r")
    data = f.read().splitlines()
    f.close()
    return data