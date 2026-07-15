class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #We can have a bfs of Pacific and bfs of Atlantic and append to a set and return a matching set.

        from collections import deque

        pacificQ = deque()
        atlanticQ = deque()

        pacificSet = set()
        atlanticSet = set()

        rows = len(heights)
        cols = len(heights[0])

        directions =[[-1, 0], [1, 0], [0, -1], [0, 1]]

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacificQ.append([r,c])
                    pacificSet.add((r,c))
                if r == rows - 1 or c == cols - 1:
                    atlanticQ.append([r,c])
                    atlanticSet.add((r,c))
        def bfs(q, s):
            while q:
                for i in range(len(q)):
                    oR, oC = q.popleft()
                    for d in directions:
                        r, c = oR + d[0], oC + d[1]
                        if (min(r, c) < 0
                            or r >= rows
                            or c >= cols
                            or heights[oR][oC] > heights[r][c]
                            or (r, c) in s):
                            continue
                        q.append([r,c])
                        s.add((r, c))
            return s
        
        overlap = list(bfs(pacificQ, pacificSet) & bfs(atlanticQ, atlanticSet))
        return [list(pos) for pos in overlap]


