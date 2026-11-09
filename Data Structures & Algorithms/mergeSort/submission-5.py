# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
#  3,8,6,2,9,12,1
#0-6 m=3
# 3,8,6,2 9,12,1
# 3,8 6,2 9,12 1
# 3 8 6 2 9 12 1
# 3 8 2 6 9 12 1
# 2 3 6 8 1 9 12
# 1 2 3 6 8 9 12
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
    def mergeS(self,arr,l,r):
        if l>r:
            return []
        if l==r:
            return [arr[l]]
        m=(r+l)//2
        left=self.mergeS(arr,l,m)
        right=self.mergeS(arr,m+1,r)
        return self.mergeTwoList(left,right)

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        pairs[:]=self.mergeS(pairs,0,len(pairs)-1)
        return pairs
