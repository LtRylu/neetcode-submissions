class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append([heights[0], 0])

        # [Bar heights, index of the left side of the bar]
        # only in ascending order, each value is also unique

        maxArea = 0
        #current max area

        #loop through the heights
        #i and val simulate the right side of our current area we are calculating
        for i, val in enumerate(heights):
            # append current bar
            stack.append([val, i])
            # while there is a stack, and while the current value is less than or equal to the top of the stack
            while stack and val <= stack[-1][0]:
                
                height, start  = stack.pop()
                area = height * (i - start)
                maxArea = max(maxArea,area)
            
            stack.append([val, start])
            
        #if there is a remaining stack we want to calculate the max area which is just the heigh of the smaller bar and the distance from the right.
        while stack:
            left = stack.pop()
            maxArea = max(maxArea, left[0] * (len(heights) - left[1]))
        return maxArea