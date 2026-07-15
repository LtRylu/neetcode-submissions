class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        islands = set()

        def dfs(r, c):
            if (min(r, c) < 0 
                or r >= len(grid) 
                or c >= len(grid[0]) 
                or grid[r][c] == '0' 
                or (r,c) in islands):
                    return False
            else:
                islands.add((r,c))
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
                return True
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(r, c):
                    count += 1

        return count