class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        def dfs(p, left, right):
            l = left + nums[p]
            r = right - nums[p]
            if l == r:
                return True
            if l < r:
                for i in range(p + 1, len(nums)):
                    if dfs(i, l, r):
                        return True
            return False
        for i in range(len(nums)):
            if dfs(i,0,s):
                return True
        return False