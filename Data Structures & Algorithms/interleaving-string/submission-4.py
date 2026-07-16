class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def dfs(a, b):
            
            if (a,b) in dp:
                return dp[(a,b)]
            
            k = a + b

            if k >= len(s3):
                return True
            if a < len(s1) and s3[k] == s1[a] and dfs(a + 1, b):
                return True
            if b < len(s2) and s3[k] == s2[b] and dfs(a, b + 1):
                return True
            dp[(a,b)] = False
            return False

        return dfs(0, 0)