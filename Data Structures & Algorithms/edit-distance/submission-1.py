class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}

        def dfs(a, b):
            if b == len(word2) or a == len(word1):
                return len(word1) - a + len(word2) - b
            if (a, b) in dp:
                return dp[(a,b)]
            if word1[a] == word2[b]:
                replace = dfs(a + 1, b + 1)
            else:
                replace = dfs(a + 1, b + 1) + 1
            ins = 1 + dfs(a, b + 1)
            delete = 1 + dfs(a + 1, b)
            dp[(a,b)] = min(replace, ins, delete)
            return dp[(a,b)]
        return dfs(0, 0)
