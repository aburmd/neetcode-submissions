class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ec={}
        freq=[[] for i in range(len(nums)+1)]
        res=[]
        cnt=0
        for n in nums:
            ec[n]=1+ec.get(n,0)
        for n,c in ec.items():
            freq[c].append(n)
        for earr in freq[::-1]:
            for e in earr:
                res.append(e)
                if len(res)==k:
                    return res
        return -1
        