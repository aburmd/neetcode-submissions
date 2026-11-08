# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickS(self, arr,l,r):
        if l>=r:
            return
        pivot=arr[r]
        point=l
        for i in range(l,r):
            if arr[i].key<pivot.key:
                arr[i],arr[point]=arr[point],arr[i]
                point+=1
        arr[point],arr[r]=arr[r],arr[point]
        self.quickS(arr,l,point-1)
        self.quickS(arr,point+1,r)
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickS(pairs,0,len(pairs)-1)
        return pairs
        