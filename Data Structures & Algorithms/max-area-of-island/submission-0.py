class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = set()
        maxArea = 0
        def dfs(r, c, grid, islands, subset):
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return False
            elif (r,c) in islands:
                return False
            elif (r,c) in subset:
                return False
            else:
                subset.add((r,c))
                dfs(r+1, c, grid, islands, subset)
                dfs(r-1, c, grid, islands, subset)
                dfs(r, c+1, grid, islands, subset)
                dfs(r, c-1, grid, islands, subset)

                return True
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                subset = set()
                if dfs(r, c, grid, islands, subset):
                    islands.update(subset)
                    maxArea = max(maxArea, len(subset))
        return maxArea