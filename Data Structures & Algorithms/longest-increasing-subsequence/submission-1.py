class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        stor = [0] * len(nums)
        def recursive(i):
            if stor[i] == 0:
                stor[i] = 1
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        stor[i] = max(stor[i], 1 + recursive(j))
            return stor[i]
        for i in range(len(nums)):
            res = max(res, recursive(i))
        return res
        
        