# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
#  3,8,6,2,9,12,1 

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res=[]
        for i in range(len(pairs)):
            if i<=0:
                res.append(pairs[:])
                continue
            j=i-1
            while j>=0 and pairs[j].key>pairs[j+1].key:
                pairs[j],pairs[j+1]=pairs[j+1],pairs[j]
                j-=1
            res.append(pairs[:])
        return res
            