class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS,countT={},{}
        for i,c in enumerate(s):
            countS[c]=1+countS.get(c,0)
            countT[t[i]]=1+countT.get(t[i],0)
        for c,n in countS.items():
            if c not in countT or n!=countT[c]:
                return False
        return True
        