class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l+=1
            res=max(res,r-l+1)
            visited.add(s[r])
        return res

        