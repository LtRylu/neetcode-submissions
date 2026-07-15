class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, i in enumerate(nums):
            check = target - i
            for jdx, j in enumerate(nums[idx+1:], start=idx+1):
                if j == check:
                    return [idx, jdx]
        return False