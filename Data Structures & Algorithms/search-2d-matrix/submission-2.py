class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        first = 0
        last = rows * columns - 1 #since first int of every row < last int of prev row - one big array
        while first <= last:
            middle = (first + last) // 2
            row = middle // columns
            column = middle % columns
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                first = middle + 1
            else:
                last = middle - 1

        return False