class Solution:

    def euDist(self, x, y):
        return math.sqrt(x**2+y**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i, val in enumerate(points):
            dist.append([-self.euDist(val[0], val[1]), i])
        heapq.heapify(dist)

        while k < len(dist):
            heapq.heappop(dist)
        vals = []
        for i in dist:
            vals.append(points[i[1]])
        return vals