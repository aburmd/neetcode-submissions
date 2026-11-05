class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        existing=set(nums)
        for i,n in enumerate(nums):
            if n-1 in existing:
                continue
            cur=0
            while n in existing:
                cur+=1
                res=max(res,cur)
                n+=1
        return res

        