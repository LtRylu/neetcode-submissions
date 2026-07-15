class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        t = len(nums) - 1
        h = 0
        if len(nums) == 0:
            return 0
        while h <= t:
            while t >= 0 and nums[t] == val:
                t -= 1
            if h < t and nums[h] == val:
                nums[h] = nums[t]
                nums[t] = val
                t -= 1
            h += 1
        return t + 1