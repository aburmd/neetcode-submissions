class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res,dct=0,{}
        for r in range(len(s)):
            dct[s[r]]=1+dct.get(s[r],0)
            maxC=0
            for c,v in dct.items():
                maxC=max(maxC,v)
            if r-l+1-maxC-k<=0:
                res=max(res,r-l+1)
            else:
                dct[s[l]]-=1
                l+=1
        return res
        