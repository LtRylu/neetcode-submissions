class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        dp[0] = 1
        for i in nums:
            newDP = {}
            for j in dp.keys():
                newDP[j + i] = newDP.get(j + i, 0) + dp[j]
                newDP[j - i] = newDP.get(j - i, 0) + dp[j]
            dp = newDP.copy()
        return dp.get(target, 0)