class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        dctT,dctS={},{}
        for c in t:
            dctT[c]=1+dctT.get(c,0)
        curMatch,reqMatch=0,len(dctT)
        l=0
        posRes=None
        for r in range(len(s)):
            if s[r] in dctT:
                dctS[s[r]]=1+dctS.get(s[r],0)
                if dctT[s[r]]==dctS.get(s[r],0):
                    curMatch+=1
                if curMatch==reqMatch:
                    if not posRes:
                        posRes=s[l:r+1]
                    elif posRes and len(posRes)>r-l+1:
                        posRes=s[l:r+1]
            while curMatch==reqMatch and l<=r:
                if posRes and len(posRes)>r-l+1:
                    posRes=s[l:r+1]
                if s[l] in dctT:
                    dctS[s[l]]-=1
                    if dctS[s[l]] < dctT[s[l]]:
                        curMatch-=1
                l+=1
        return posRes if posRes else ''

            


        

        