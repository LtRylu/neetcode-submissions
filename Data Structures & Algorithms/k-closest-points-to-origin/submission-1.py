class Solution:

    def euDist(self, x, y):
        return math.sqrt(x**2+y**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        heapq.heapify(dist)
        for i, val in enumerate(points):
            heapq.heappush(dist, [-self.euDist(val[0], val[1]), i])
            if k < len(dist):
                heapq.heappop(dist)
        vals = []
        for i in dist:
            vals.append(points[i[1]])
        return vals