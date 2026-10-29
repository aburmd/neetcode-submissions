class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        existing=set()
        l=0
        maxlength=0
        for r,c in enumerate(s):
            while c in existing:
                existing.remove(s[l])
                l+=1
            existing.add(c)
            maxlength=max(maxlength,r-l+1)
        return maxlength