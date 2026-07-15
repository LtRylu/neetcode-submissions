class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones] #o(n)
        heapq.heapify(stones) # o(n)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x - y < 0:
                heapq.heappush(stones, x-y)
        if len(stones) > 0:
            return -stones[0]
        else:
            return 0



        