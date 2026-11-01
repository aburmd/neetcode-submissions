# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeList(self,l1,l2):
        dummy=ListNode(0,None)
        tail=dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next=l1
                l1=l1.next
                tail=tail.next
            else:
                tail.next=l2
                l2=l2.next
                tail=tail.next
        if not l1:
            tail.next=l2
        if not l2:
            tail.next=l1
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            mergedList=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1 < len(lists) else None
                res=self.mergeList(l1,l2)
                mergedList.append(res)
            lists=mergedList
        return lists[-1]