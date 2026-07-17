class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        cur = []

        for i in nums:
            for j in range(len(res)):
                sub = res[j].copy()
                sub.append(i)
                res.append(sub)
        return res