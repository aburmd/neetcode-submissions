# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 0-1-2-3-4-None

# pre      None           0-None         
# nextNode None           0-None 
# pre      0-1-2-3-4-None 1-2-3-4-None
# pre.next 0-None         1-0-None 
# cur      1-2-3-4-None   2-3-4-None

class Solution:
    def reverse(self, head):
        cur,pre=head,None
        while cur:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=self.reverse(slow.next)
        slow.next=None
        first=head
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
        return None


        
        