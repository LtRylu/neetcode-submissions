class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        prev_target = None
        for idx, num in enumerate(nums):
            if idx > length - 3:
                break
            l = idx+1
            r = length - 1
            target = -num
            if prev_target == target:
                continue
            prev_target = target
            while l < r:
                while l < r and nums[l] + nums[r] != target:
                    if nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
                if l < r and nums[l] + nums[r] == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res
                
            


        