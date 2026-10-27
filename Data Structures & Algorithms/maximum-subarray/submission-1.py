class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum,curSum=nums[0],0
        l,r=0,0
        maxL,maxR=0,0
        for r in range(len(nums)):
            if curSum < 0:
                l=r
                curSum=0
            curSum+=nums[r]
            if curSum > maxSum:
                maxSum=curSum
                maxL,maxR=l,r
        return maxSum


        