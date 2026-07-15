class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2
        while left < right:
            middle = (left + right) // 2

            if nums[middle] < nums[left] and nums[middle] < nums[right]:
                if nums[left] < nums[right]:
                    left = middle
                else:
                    right = middle
            elif nums[middle] > nums[right] and nums[middle] > nums[left]:
                if nums[left] > nums[right]:
                    left = middle
                else:
                    right = middle
            else:
                return min(nums[left], nums[right])
        return nums[middle]