class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for i in nums:
            colors[i] += 1
        index = 0
        color = 0
        while color < len(colors):
            while colors[color] > 0:
                nums[index] = color
                colors[color] -= 1
                index += 1
            color += 1

