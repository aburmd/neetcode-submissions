# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickS(self, pairs,l,r):
        if l>=r:
            return
        pivot=pairs[r]
        shift=l
        for i in range(l,r):
            if pairs[i].key<pivot.key:
                tmp=pairs[i]
                pairs[i]=pairs[shift]
                pairs[shift]=tmp
                shift+=1
        tmp=pairs[shift]
        pairs[shift]=pairs[r]
        pairs[r]=tmp
        self.quickS(pairs,l,shift-1)
        self.quickS(pairs,shift+1,r)
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickS(pairs,0,len(pairs)-1)
        return pairs

                
        
        