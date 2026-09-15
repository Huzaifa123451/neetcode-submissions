class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sublist in matrix:
            first = 0
            last = len(sublist) - 1
            while first <= last:
                middle = (first + last) // 2
                if sublist[middle] == target:
                    return True
                elif sublist[middle] < target:
                    first = middle + 1
                else:
                    last = middle - 1
        return False