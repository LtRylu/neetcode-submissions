class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0] * COLS
        prevRow[-1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if c == COLS - 1:
                    right = 0
                else:
                    right = prevRow[c + 1]
                if obstacleGrid[r][c] == 1:
                    prevRow[c] = 0
                else:
                    prevRow[c] = prevRow[c] + right
        return prevRow[0]



