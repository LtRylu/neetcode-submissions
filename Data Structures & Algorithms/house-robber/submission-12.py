class Solution:

    def rob(self, nums: List[int]) -> int:
            def memoization(n, cache):
                if n >= len(nums):
                    return 0
                if n == len(nums)-1 or n == len(nums)-2:
                    return nums[n]
                if n in cache:
                    return cache[n]
                
                cache[n] = nums[n] + max(memoization(n+2, cache), memoization(n+3, cache))
                return cache[n]
            return max(memoization(1, {}), memoization(0, {}))

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
            