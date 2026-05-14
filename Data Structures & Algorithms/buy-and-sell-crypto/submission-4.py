class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        l = 0

        for r in prices:
            if r == prices[l]:
                continue
            
            if r > prices[l]:
                maxP = max(maxP, (r - prices[l]))
            else:
                l = prices.index(r)

        return maxP
            