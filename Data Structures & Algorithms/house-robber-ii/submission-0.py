class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(arr):
            rob1, rob2 = 0, 0
            for n in arr:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))