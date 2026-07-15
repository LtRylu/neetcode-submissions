class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        q = deque()
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        layer = 1
        while q:
            for i in range(len(q)):
                oR, oC = q.popleft()
                for d in directions:
                    r, c = oR + d[0], oC + d[1]
                    if (min(r, c) < 0 
                        or r >= ROWS
                        or c >= COLS
                        or grid[r][c] != INF):
                        continue
                    q.append((r,c))
                    grid[r][c] = layer
            layer += 1

