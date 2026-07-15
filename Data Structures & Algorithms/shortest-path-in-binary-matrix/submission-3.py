class Solution:
    

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1], [1,1], [1, -1], [-1, -1], [-1, 1]]

        from collections import deque
        q = deque()
        visit = set()
        q.append((0, 0))
        visit.add((0, 0))
        length = 1

        while q:
            for i in range(len(q)):
                cur = q.popleft()
                oR, oC = cur[0], cur[1]
                for d in directions:
                    r, c = oR + d[0], oC + d[1]
                    if (min(r, c) < 0 
                        or r >= ROWS 
                        or c >= COLS 
                        or grid[r][c] == 1
                        or (r, c) in visit):
                            continue
                    elif r == ROWS - 1 and c == COLS - 1:
                        return length + 1
                    else: 
                        q.append((r, c))
                        visit.add((r, c))
            length += 1

        return -1
                    
                

