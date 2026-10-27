class Solution:
    def __init__(self):
        self.prefixDct={}
        self.suffixDct={}
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def prefixSum(i):
            if i in self.prefixDct:
                return self.prefixDct[i]
            curSum,preSum=nums[0],nums[0]
            if i==0:
                return curSum
            for r in range(1,i+1):
                curSum+=nums[r]
                if curSum < 0:
                    continue
                preSum=max(curSum,preSum)
            self.prefixDct[i]=max(preSum,curSum)
            return self.prefixDct[i]
        def suffixSum(i):
            if i in self.suffixDct:
                return self.suffixDct[i]
            curSum,preSum=nums[len(nums)-1],nums[len(nums)-1]
            if i==len(nums)-1:
                return curSum
            for r in range(len(nums)-2,i-1,-1):
                curSum+=nums[r]
                if curSum < 0:
                    continue
                preSum=max(curSum,preSum)
            self.suffixDct[i]=max(preSum,curSum)
            return self.suffixDct[i]
        maxSum,curSum=nums[0],0
        for i in range(len(nums)):
            if curSum < 0:
                curSum=0
            curSum+=nums[i]
            maxSum=max(curSum,maxSum)
            if i==len(nums)-1:
                continue
            maxSum = max(maxSum, prefixSum(i) + suffixSum(i+1))
        return maxSum
            


                




        