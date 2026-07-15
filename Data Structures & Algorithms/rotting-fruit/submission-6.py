class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])


        freshB = 0
        q = deque()
        length = -1
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    freshB += 1

        if freshB == 0:
            return 0
        while q:
            for i in range(len(q)):
                oR, oC = q.popleft()
                for d in directions:
                    r, c = oR + d[0], oC + d[1]
                    if (min(r, c) < 0 
                        or r >= ROWS
                        or c >= COLS
                        or grid[r][c] != 1):
                        continue
                    q.append((r,c))
                    freshB -= 1
                    grid[r][c] = 2
            length += 1

        if freshB > 0:
            return -1
        else:
            return length

        




            
