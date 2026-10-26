class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct={}
        for s in strs:
            anaGroup=[0]*26
            for c in s:
                anaGroup[ord(c)-ord('a')]+=1
            if tuple(anaGroup) not in dct:
                dct[tuple(anaGroup)]=[s]
            else:
                dct[tuple(anaGroup)].append(s)
        return list(dct.values())