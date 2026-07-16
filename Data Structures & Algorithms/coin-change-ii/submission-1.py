class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(val, c):
            if val == amount:
                return 1
            if val > amount or c == len(coins):
                return 0
            if (val, c) in dp:
                return dp[(val, c)]

            dp[(val, c)] = dfs(val + coins[c], c) + dfs(val, c + 1)
            return dp[(val, c)]

        return dfs(0, 0)