class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dctS,dctT={},{}
        for i,c in enumerate(s):
            dctS[c]=1+dctS.get(c,0)
            dctT[t[i]]=1+dctT.get(t[i],0)
        for c,v in dctS.items():
            if v!=dctT.get(c,0):
                return False
        return True 