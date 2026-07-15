class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = 0
        l, r = 0, len(heights) - 1
        while l < r:
            if heights[l] < heights[r]:
                max_height = max(max_height, (r-l) * heights[l]) 
                l += 1
            else:
                max_height =  max(max_height, (r-l) * heights[r]) 
                r -= 1
        return max_height
        