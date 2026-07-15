class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        row = [0] * COLS
        row[-1] = 1

        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                
                if obstacleGrid[r][c] == 1:
                    row[c] = 0
                elif c < COLS - 1:
                    row[c] = row[c] + row[c + 1]
                else:
                    row[c] = row[c]


        return row[0]



