class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False
        
        t = s // 2
        LIS = [False] * (t + 1)
        LIS[0] = True

        for i in nums:
            for j in range(t - i, -1, -1):
                if LIS[j]:
                    LIS[j + i] = True
        return LIS[-1]