class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        kth = []

        for i in nums:
            heapq.heappush(kth, i)
            if len(kth) > k:
                heapq.heappop(kth)

        return kth[0]
        