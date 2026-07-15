class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False
        
        t = s // 2
        LIS = set()
        LIS.add(0)

        for i in nums:
            cur = []
            for j in LIS:
                if j + i <= t:
                    cur.append(j + i)
            LIS.update(cur)
        return t in LIS