class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
    
        for i, val in enumerate(heights):
            stack.append([val, i])
            while stack and val <= stack[-1][0]:

                height, start  = stack.pop()
                area = height * (i - start)
                maxArea = max(maxArea, area)
            
            stack.append([val, start])
        while stack:
            left = stack.pop()
            maxArea = max(maxArea, left[0] * (len(heights) - left[1]))
        return maxArea