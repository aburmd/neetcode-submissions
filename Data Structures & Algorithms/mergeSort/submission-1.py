# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSortedInput(self,arr1,arr2):
        i,j=0,0
        res=[]
        while i<len(arr1) and j<len(arr2):
            if arr1[i].key<=arr2[j].key:
                res.append(arr1[i])
                i+=1
            else:
                res.append(arr2[j])
                j+=1
        while i<len(arr1):
            res.append(arr1[i])
            i+=1
        while j<len(arr2):
            res.append(arr2[j])
            j+=1
        return res        

    def mSort(self,arr,l,r):
        if l>r:
            return []
        if l==r:
            return [arr[l]]
        m=(l+r)//2
        arr1=self.mSort(arr,l,m)
        arr2=self.mSort(arr,m+1,r)
        return self.mergeSortedInput(arr1,arr2)

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        l,r=0,len(pairs)-1
        return self.mSort(pairs,l,r)