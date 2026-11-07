# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head):
        curr,prev=head,None
        while curr:
            tmpNode=curr.next
            curr.next=prev
            prev=curr
            curr=tmpNode
        return prev
    def mergeList(self,first,second):
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
        return None

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast,first=head,head.next,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=self.reverseList(slow.next)
        slow.next=None
        self.mergeList(first,second)


        
        