class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        
        for c in tasks:
            freq[c] = 1 + freq.get(c, 0)
        import heapq
        from collections import deque

        heap = [-v for v in freq.values()]

        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            if heap:
                cur = heapq.heappop(heap) + 1
                if cur < 0:
                    q.append((cur, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
            time += 1

        return time