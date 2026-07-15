class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        lenT = len(temperatures)
        output = [0] * lenT
        for i in range(lenT):
            while stack and temperatures[i] > stack[-1][0]:
                curT, curI = stack.pop()
                output[curI] = i - curI
            stack.append([temperatures[i], i])
        return output