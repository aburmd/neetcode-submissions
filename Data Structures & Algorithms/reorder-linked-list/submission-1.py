# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 0-1-2-3-4-None

class Solution:
    def reverseList(self,head):
        curr,prev=head,None
        while curr:
            tmp1=curr.next
            curr.next=prev
            prev=curr
            curr=tmp1
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        first=head
        second=self.reverseList(slow.next)
        slow.next=None
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
        return None


        
        