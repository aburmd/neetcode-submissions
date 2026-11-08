# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeArray(self,left,right):
        i=j=0
        res=[]
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
    def mSort(self,arr,l,r):
        if l>r:
            return []
        if l==r:
            return [arr[l]]
        m=(l+r)//2
        left=self.mSort(arr,l,m)
        right=self.mSort(arr,m+1,r)
        return self.mergeArray(left,right)
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mSort(pairs,0,len(pairs)-1)
