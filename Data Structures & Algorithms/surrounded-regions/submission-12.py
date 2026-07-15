class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = set()

        safe = []
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1 and board[r][c] == "O":
                     safe.append((r, c))
        def dfs(r, c):
            # base case
            if (min(r, c) < 0
                or r >= rows
                or c >= cols
                or board[r][c] == "X"
                or (r, c) in visited):
                return
            visited.add((r, c))

            down, up, left, right = dfs(r + 1, c), dfs(r - 1, c), dfs(r, c + 1), dfs(r, c - 1)
        for s in safe:
            dfs(s[0], s[1])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
        


