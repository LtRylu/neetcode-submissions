class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(val, c):
            if val == 0:
                return 1
            if val < 0:
                return 0
            if (val, c) in dp:
                return dp[(val, c)]
            dp[(val, c)] = 0

            for i in range(c, len(coins)):
                dp[(val, c)] += dfs(val - coins[i], i)
            return dp[(val, c)]

        return dfs(amount, 0)