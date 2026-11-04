class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        dctT,dctS={},{}
        for c in t:
            dctT[c]=1+dctT.get(c,0)
        curMatch,reqMatch,l=0,len(dctT),0
        res=None
        for r in range(len(s)):
            if s[r] in dctT:
                dctS[s[r]]=1+dctS.get(s[r],0)
            if s[r] in dctT and dctT[s[r]]==dctS.get(s[r],0):
                curMatch+=1
            while curMatch==reqMatch:
                if not res:
                    res=l,r
                elif res[1]-res[0] > r-l:
                    res=l,r
                if s[l] in dctS:
                    dctS[s[l]]=-1+dctS.get(s[l],0)
                if s[l] in dctT and dctT[s[l]]==1+dctS.get(s[l],0):
                    curMatch-=1
                l+=1
        return s[res[0]:res[1]+1] if res else ''

