class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for s in strs:
            anagrams=[0]*26
            for c in s:
                anagrams[ord(c)-ord('a')]+=1
            if tuple(anagrams) not in res:
                res[tuple(anagrams)]=[]
            res[tuple(anagrams)].append(s)
        return list(res.values())