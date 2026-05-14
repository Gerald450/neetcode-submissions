class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = selling price - buying price
        maxd = 0
        for index, value in enumerate(prices):
            l = index + 1
            while l < len(prices):
                d = prices[l] - value
                maxd = max(maxd, d)
                l += 1
        return maxd
            