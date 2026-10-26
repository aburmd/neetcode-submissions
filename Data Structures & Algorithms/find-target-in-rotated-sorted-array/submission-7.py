class Solution:
    def bs(self, nums, target, indexshift):
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target < nums[m]:
                r=m-1
            elif nums[m] < target:
                l=m+1
            else:
                return m+indexshift
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m] < nums[r]:
                r=m
            else:
                l=m+1
        midVal=l
        if midVal and nums[0] <= target:
            return self.bs(nums[0:midVal],target,0)
        else:
            return self.bs(nums[midVal:len(nums)],target,midVal)


            