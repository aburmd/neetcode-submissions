class Solution:

    def encode(self, strs: List[str]) -> str:       
        res=''
        if len(strs)<=0:
            return ''
        for s in strs:
            res+=str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        if len(s)<=0:
            return res
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            cnt=int(s[i:j])
            res.append(s[j+1:j+cnt+1])
            i=j+cnt+1
        return res
