class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, h = 0, len(matrix) * len(matrix[0]) - 1

        while l <= h:
            m = (l + h) // 2
            mr, mc = m // len(matrix[0]), m % len(matrix[0])

            if target > matrix[mr][mc]:
                l = m + 1
            elif target < matrix[mr][mc]:
                h = m - 1
            else:
                return True
            
        return False
