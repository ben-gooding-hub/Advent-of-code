from typing import Optional

def isInBounds(position: tuple[int, int], xYMax: tuple[int, int]) -> bool:
    return 0 <= position[0] < xYMax[0] and 0 <= position[1] < xYMax[1]

def getChar(x: int, y: int, data: list[str], xYMax: tuple[int, int]) -> Optional[str]:
    if not isInBounds((x, y), xYMax):
        return None
    return data[y][x]