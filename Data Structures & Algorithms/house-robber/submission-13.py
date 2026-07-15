class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        if n < 3:
            return max(nums[0], nums[1])
        

        dp = [nums[0], nums[1], nums[0] + nums[2]]
        i = 3
        while i < n:
            tmp1 = dp[2]
            dp[2] = nums[i] + max(dp[0], dp[1])
            tmp = dp[1]
            dp[0], dp[1] = tmp, tmp1
            i += 1
        return max(dp[1], dp[2])
            