class Solution:
    def mergeSort(self,nums,l,r):
        if r-l+1==1:
            return [nums[l]]
        m=(l+r)//2
        first=self.mergeSort(nums,l,m)
        second=self.mergeSort(nums,m+1,r)
        return self.mergeS(first,second)
    def mergeS(self,first,second):
        res=[]
        i,j=0,0
        while i<len(first) and j<len(second):
            if first[i]<second[j]:
                res.append(first[i])
                i+=1
            else:
                res.append(second[j])
                j+=1
        while i<len(first):
            res.append(first[i])
            i+=1
        while j<len(second):
            res.append(second[j])
            j+=1
        return res

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,m+n):
            nums1[i]=nums2[i-m]
        if m+n > 0:
            nums1[:]=self.mergeSort(nums1,0,m+n-1)

        