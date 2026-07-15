class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        k_list = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for n, c in count.items():
            k_list[c].append(n)
        res = []
        for i in range(len(nums), 0, -1):
            for j in k_list[i]:
                res.append(j)
                if len(res) == k:
                    return res
