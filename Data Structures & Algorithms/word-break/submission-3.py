class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        MKL = 0
        keySet = set()
        lengths = set()

        dp = [None for _ in range(len(s) + 1)]

        for i in wordDict:
            lengths.add(len(i))
            keySet.add(i)
        
        def memoization(p):
            res = False
            if p == len(s):
                res = True
            for i in lengths:
                if p + i <= len(s) and dp[p] is not False and s[p:p+i] in keySet:
                    res = res or memoization(p+i)
            dp[p] = res
            return res
        return memoization(0)

