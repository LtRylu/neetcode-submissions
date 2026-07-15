class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshB = {}

        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def bfs(r, c):
            from collections import deque
            length = 1
            q = deque()
            q.append((r, c))

            while q:
                for i in range(len(q)):
                    oR, oC = q.popleft()
                    for d in directions:
                        r, c = oR + d[0], oC + d[1]
                        if (min(r, c) < 0 
                            or r >= ROWS 
                            or c >= COLS 
                            or grid[r][c] == 0 
                            or grid[r][c] == 2):
                            continue

                        if ((r,c) not in freshB 
                            or freshB[(r,c)] == -1 
                            or length < freshB[(r,c)]):
                            freshB[(r,c)] = length
                            q.append((r,c))
                length += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    bfs(r,c)
                elif grid[r][c] == 1 and (r,c) not in freshB:
                    freshB[(r,c)] = -1
        min_value = 0
        max_value = 0
        for value in freshB.values():
            min_value = min(min_value, value)
            max_value = max(max_value, value)
        if min_value > -1:
            return max_value
        else:
            return -1
        




            
