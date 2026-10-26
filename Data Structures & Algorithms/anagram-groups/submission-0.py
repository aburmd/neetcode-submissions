class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct={}
        for s in strs:
            grpAnagram=[0]*26
            for c in s:
                grpAnagram[ord(c)-ord('a')]+=1
            if tuple(grpAnagram) not in dct:
                dct[tuple(grpAnagram)]=[s]
            else:
                dct[tuple(grpAnagram)].append(s)
        return list(dct.values())
        