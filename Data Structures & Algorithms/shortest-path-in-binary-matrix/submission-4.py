class Solution:
    

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #edge case
        if grid[0][0] == 1:
            return -1
        
        #define borders + possible path directions
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1], [1,1], [1, -1], [-1, -1], [-1, 1]]

        from collections import deque

        # possible points to visit, q is used for BFS to check layers in order
        q = deque()
        # need a set to check if we visited the point already
        visit = set()
        # establish first point
        q.append((0, 0))
        visit.add((0, 0))
        length = 1

        #while q non empty, meaning that we still have possible points to expand off of
        while q:
            # iterate through current layer
            for i in range(len(q)):
                # look at current point
                cur = q.popleft()
                oR, oC = cur[0], cur[1]

                # explore every direction from current point
                for d in directions:
                    r, c = oR + d[0], oC + d[1]
                    # if not a valid point, skip and do nothing
                    if (min(r, c) < 0 
                        or r >= ROWS 
                        or c >= COLS 
                        or grid[r][c] == 1
                        or (r, c) in visit):
                            continue
                    # if we reach desired point return current length
                    elif r == ROWS - 1 and c == COLS - 1:
                        return length + 1
                    # if we encounter a new possible point we add to the next layer / q
                    else: 
                        q.append((r, c))
                        visit.add((r, c))
            #after iterating through entire layer we increase length by 1
            length += 1

        # we were not able to reach desired point bc there are no more possible points to check so we return -1
        return -1
                    
                

