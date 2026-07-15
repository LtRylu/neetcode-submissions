class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        val = [None] * (amount + 1)
        val[0] = 0
        def memoization(n, cache):
            if cache[n] is not None:
                return cache[n]
            minC = float("inf")
            for c in coins:
                if n - c >= 0:
                    minC = min(1 + memoization(n - c, cache), minC)
            return minC

        for n in range(amount + 1):
            val[n] = memoization(n, val)
        
        if val[-1] != float("inf"):
            return val[-1]
        return -1


