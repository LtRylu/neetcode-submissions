class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(a, b):
            k = a + b
            if (a,b) in dp:
                return dp[(a,b)]
            if k >= len(s3):
                dp[(a,b)] = True
            elif a < len(s1) and b < len(s2) and s3[k] == s1[a] and s3[k] == s2[b]:
                dp[(a,b)] = dfs(a + 1, b) or dfs(a, b + 1)
            elif a < len(s1) and s3[k] == s1[a]:
                dp[(a,b)] = dfs(a + 1, b)
            elif b < len(s2) and s3[k] == s2[b]:
                dp[(a,b)] = dfs(a, b + 1)
            else:
                dp[(a,b)] = False
            return dp[(a,b)]
        return dfs(0, 0)