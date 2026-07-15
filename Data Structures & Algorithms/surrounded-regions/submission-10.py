class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(r, c, component):
            # base case
            if (min(r, c) < 0
                or r >= rows
                or c >= cols):
                return False
            if board[r][c] == "X" or (r, c) in visited:
                return True
        
            visited.add((r, c))
            component.append((r, c))

            down, up, left, right = dfs(r + 1, c, component), dfs(r - 1, c, component), dfs(r, c + 1, component), dfs(r, c - 1, component)
            if down and up and left and right:
                return True
            return False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    component = []
                    if dfs(r, c, component):
                        for row, col in component:
                            board[row][col] = "X"
        


