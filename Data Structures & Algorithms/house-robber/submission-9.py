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