class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        keySet = set()
        lengths = set()
        dp = [None for _ in range(len(s) + 1)]
        dp[len(s)] = True

        for i in wordDict:
            lengths.add(len(i))
            keySet.add(i)
        
        def memoization(p):
            if dp[p] is not None:
                return dp[p]
            dp[p] = False
            for i in lengths:
                if p + i <= len(s) and s[p:p+i] in keySet:
                    dp[p] = dp[p] or memoization(p+i)
            return dp[p]
        return memoization(0)

