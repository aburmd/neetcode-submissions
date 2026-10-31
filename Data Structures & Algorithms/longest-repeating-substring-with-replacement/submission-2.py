class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)<=1:
            return len(s)
        l,longest=0,0
        dct={}
        for r,c in enumerate(s):
            dct[c]=1+dct.get(c,0)
            maxW=max(dct.values())
            if r-l+1 - maxW <= k:
                longest=max(longest,r-l+1)
            else:
                dct[s[l]]-=1
                l+=1
        return longest



        