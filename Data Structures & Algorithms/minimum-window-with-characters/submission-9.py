class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ''
        dctT,dctS={},{}
        for c in t:
            dctT[c]=1+dctT.get(c,0)
        l,curMatch,resMatch=0,0,len(dctT)
        resPos=None
        for r in range(len(s)):
            dctS[s[r]]=1+dctS.get(s[r],0)
            if s[r] in dctT and dctT[s[r]]==dctS[s[r]]:
                curMatch+=1
            while curMatch==resMatch:
                if not resPos:
                    resPos=l,r+1
                elif resPos and resPos[1]-resPos[0]>r-l+1:
                    resPos=l,r+1
                dctS[s[l]]-=1
                if s[l] in dctT and 1+dctS[s[l]]==dctT[s[l]]:
                    curMatch-=1
                l+=1
        return s[resPos[0]:resPos[1]] if resPos else ''

            


        

        