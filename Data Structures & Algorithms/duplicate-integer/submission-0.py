class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing=set()
        for n in nums:
            if n in existing:
                return True
            existing.add(n)
        return False
        