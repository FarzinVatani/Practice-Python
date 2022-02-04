from typing import Optional, Union, Tuple, List
Digit = Union[int, float]

def swapOrBreak(leftNum: Digit , rightNum: Digit) -> Optional[Tuple[Digit, Digit]]:
    return (rightNum, leftNum) if rightNum < leftNum else None

def insertionSort(nNumber: List[int]) -> List[int]:
    nTempNum: List[int] = nNumber.copy()

    for i in range(1, len(nTempNum)):
        j: int = i - 1
        result: Optional[Tuple[Digit, Digit]] = (0, 0)
        while j >= 0 and result:
            if result := swapOrBreak(nTempNum[j], nTempNum[j+1]):
                (nTempNum[j], nTempNum[j+1]) = result
                j -= 1
            else:
                break
    return nTempNum
