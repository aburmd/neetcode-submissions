# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        cur,pre=head,None
        while cur:
            nextNode=pre
            pre=cur
            cur=cur.next
            pre.next=nextNode
        return pre
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        tail=self.reverseList(slow.next)
        cur=head
        maxSum=0
        while tail:
            maxSum=max(maxSum,cur.val+tail.val)
            cur=cur.next
            tail=tail.next
        return maxSum




        