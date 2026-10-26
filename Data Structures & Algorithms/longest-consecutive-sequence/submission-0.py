class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        existing=set(nums)
        longest=0
        for n in nums:
            if n-1 in existing:
                continue
            res=0
            while n in existing:
                res+=1
                n+=1
            longest=max(longest,res)
        return longest
        