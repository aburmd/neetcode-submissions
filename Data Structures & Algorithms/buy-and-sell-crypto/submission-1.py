class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,l=0,0
        for r in range(1,len(prices)):
            if prices[r]-prices[l] > 0:
                profit=max(profit,prices[r]-prices[l])
                continue
            l=r
        return profit
            