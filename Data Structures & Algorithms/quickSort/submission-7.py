# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
#  8,3,2,1,9,12,6 
class Solution:
    def quickS(self,arr,l,r):
        if l>=r:
            return
        pivot=arr[r]
        shift=l
        for i in range(l,r):
            if arr[i].key < pivot.key:
                arr[i],arr[shift]=arr[shift],arr[i]
                shift+=1
        arr[r],arr[shift]=arr[shift],arr[r]
        self.quickS(arr,l,shift-1)
        self.quickS(arr,shift+1,r)
        return arr
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickS(pairs,0,len(pairs)-1)
        return pairs
        