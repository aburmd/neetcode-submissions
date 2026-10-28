class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        profit=0
        l=0
        for r in range(1,len(prices)):
            if prices[r]-prices[l] > 0:
                profit=max(profit,prices[r]-prices[l])
            else:
                l=r
        return profit
            