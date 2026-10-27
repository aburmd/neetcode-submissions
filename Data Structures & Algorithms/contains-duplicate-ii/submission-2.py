class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        l=0
        for r in range(len(nums)):
            if nums[r] in window:
                return True
            if window and r-l+1 > k:
                window.remove(nums[l])
                l+=1
            window.add(nums[r])
        return False
