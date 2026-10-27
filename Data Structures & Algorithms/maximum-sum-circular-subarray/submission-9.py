class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def prefixSum(i):
            curSum,preSum=nums[0],nums[0]
            if i==0:
                return curSum
            for r in range(1,i+1):
                curSum+=nums[r]
                if curSum < 0:
                    continue
                preSum=max(curSum,preSum)
            return max(preSum,curSum)
        def suffixSum(i):
            curSum,preSum=nums[len(nums)-1],nums[len(nums)-1]
            if i==len(nums)-1:
                return curSum
            for r in range(len(nums)-2,i-1,-1):
                curSum+=nums[r]
                if curSum < 0:
                    continue
                preSum=max(curSum,preSum)
            return max(preSum,curSum)
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
            


                




        