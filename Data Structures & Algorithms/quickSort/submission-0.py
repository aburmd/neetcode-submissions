# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickS(self,arr,l,r):
        if l>=r:
            return arr
        pivot=arr[r]
        point=l
        for i in range(l,r):
            if arr[i].key<pivot.key:
                tmp=arr[point]
                arr[point]=arr[i]
                arr[i]=tmp
                point+=1
        arr[r]=arr[point]
        arr[point]=pivot
        self.quickS(arr,l,point-1)
        self.quickS(arr,point+1,r)
        return arr

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickS(pairs,0,len(pairs)-1)