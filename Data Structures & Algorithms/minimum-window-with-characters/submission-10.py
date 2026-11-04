class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        dctT,dctS={},{}
        res=None
        for c in t:
            dctT[c]=1+dctT.get(c,0)
        reqMatch,curMatch=len(dctT),0
        l=0
        for r in range(len(s)):
            if s[r] in dctT and dctT[s[r]]==1+dctS.get(s[r],0):
                curMatch+=1
            dctS[s[r]]=1+dctS.get(s[r],0)
            while curMatch==reqMatch:
                if not res:
                    res=l,r
                elif r-l < res[1]-res[0]:
                    res=l,r
                dctS[s[l]]=-1+dctS.get(s[l],0)
                if s[l] in dctT and dctT[s[l]]==1+dctS.get(s[l],0):
                    curMatch-=1
                l+=1
        return s[res[0]:res[1]+1] if res else ''
            
