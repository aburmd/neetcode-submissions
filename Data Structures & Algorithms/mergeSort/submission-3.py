# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeTwo(self,left,right):
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
        # return should be array 
    def mergeS(self,arr,l,r):
        if l>r:
            return []
        if l==r:
            return [arr[l]]
        m=(l+r)//2
        left=self.mergeS(arr,l,m)
        right=self.mergeS(arr,m+1,r)
        return self.mergeTwo(left,right)
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        pairs[:]=self.mergeS(pairs,0,len(pairs)-1)
        return pairs
