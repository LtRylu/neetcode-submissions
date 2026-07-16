class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        dp[0] = 1
        for i in nums:
            newDP = {}
            for key, val in dp.items():
                newDP[key + i] = newDP.get(key + i, 0) + val
                newDP[key - i] = newDP.get(key - i, 0) + val
            dp = newDP
        return dp.get(target, 0)