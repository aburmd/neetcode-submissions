# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeTwoList(self,left,right):
        res=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i].key<=right[j].key:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
    def mergeS(self,pairs,l,r):
        if l>r:
            return []
        if l==r:
            return [pairs[l]]
        m=(l+r)//2
        left=self.mergeS(pairs,l,m)
        right=self.mergeS(pairs,m+1,r)
        return self.mergeTwoList(left,right)
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        pairs[:]=self.mergeS(pairs,0,len(pairs)-1)
        return pairs
