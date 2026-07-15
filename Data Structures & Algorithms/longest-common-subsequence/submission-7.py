class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        col = len(text2)
        
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(row):
            for j in range(col):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[row - 1][col - 1]
