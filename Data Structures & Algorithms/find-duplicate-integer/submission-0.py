class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
            

            