class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP,curP=0,0
        l=0
        for r in range(len(prices)):
            if prices[l]<prices[r]:
                curP=prices[r]-prices[l]
                maxP=max(maxP,curP)
            else:
                l=r
        return maxP

        
        