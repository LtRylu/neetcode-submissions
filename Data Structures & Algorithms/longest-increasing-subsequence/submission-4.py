class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        stor = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    stor[i] = max(stor[i], 1 + stor[j])
            res = max(res, stor[i])
        return res
        
        