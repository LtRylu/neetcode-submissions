class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        price1, price2 = 0, 0
        for n in cost:
            tmp = min(price1 + n, price2 + n)
            price1 = price2
            price2 = tmp
        return min(price1, price2)