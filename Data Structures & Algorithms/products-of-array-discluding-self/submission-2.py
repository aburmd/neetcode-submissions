class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,pos=1,1
        res=[1]*(len(nums))
        for i in range(len(nums)):
            res[i]*=pre
            pre*=nums[i]
            res[len(nums)-1-i]*=pos
            pos*=nums[len(nums)-1-i]
        return res
