class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search problem
        # we know the upperbound is the max # of bananas in 1 pile
        # we know the lowerbound is always total # of bananas / the hours
        maxB = 0
        totalB = 0
        for i in piles:
            maxB = max(maxB, i)
            totalB += i
        l, r = (totalB + h - 1) // h, maxB
        valK = 0
        while l <= r:
            m = (l + r) // 2
            totalH = 0
            for b in piles:
                totalH += b // m
                if b % m > 0:
                    totalH += 1
            if totalH > h:
                l = m + 1
            else:
                r = m - 1
                valK = m
        return valK
