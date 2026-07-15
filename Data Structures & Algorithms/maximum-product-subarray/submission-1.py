class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                res = max(0, res)
                curMin, curMax = 1,1
                continue
            tmp = curMin
            curMin = min(curMax * n, curMin * n, n)
            curMax = max(tmp * n, curMax * n, n)

            res = max(curMax, res)
        return res