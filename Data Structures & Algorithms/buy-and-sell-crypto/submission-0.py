class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = prices[0]
        total = 0
        for i in prices:
            if i > high:
                high = i
                total = max(total, high-low)
            if i < low:
                low = i
                high = 0
        return total

        