class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0] * COLS
        prevRow[-1] = 1
        prevCol = [0] * ROWS

        for r in range(ROWS - 1, -1, -1):
            curRow = [0] * COLS
            for c in range(COLS - 1, -1, -1):
                if c == COLS - 1:
                    right = 0
                else:
                    right = curRow[c + 1]
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                else:
                    curRow[c] = prevRow[c] + right
            prevRow = curRow
        return prevRow[0]



