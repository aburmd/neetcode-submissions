class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for i in range(len(nums)+1)]
        dct,res={},[]
        for n in nums:
            dct[n]=1+dct.get(n,0)
        for n,c in dct.items():
            freq[c].append(n)
        for e in freq[::-1]:
            for n in e:
                res.append(n)
                if len(res)==k:
                    return res
        