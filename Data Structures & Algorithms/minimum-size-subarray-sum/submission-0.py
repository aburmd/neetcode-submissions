class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength=len(nums)+1
        l=0
        curSum=0
        for r in range(len(nums)):
            curSum+=nums[r]
            while curSum>=target:
                minLength=min(minLength,r-l+1)
                curSum-=nums[l]
                l+=1
        return minLength if minLength < len(nums)+1 else 0

        