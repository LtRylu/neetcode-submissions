class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        stor = [1] * len(nums)
        stor[-1] = 1
        def recursive(i):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    stor[i] = max(stor[i], 1 + stor[j])
            return stor[i]
        for i in range(len(nums) - 1, -1, -1):
            res = max(res, recursive(i))
        return res
        
        