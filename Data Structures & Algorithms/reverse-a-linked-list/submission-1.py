# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        while curr:
            head=prev
            prev=curr
            curr=curr.next
            prev.next=head
        return prev

# curr,head0-1-2-3- prev-
# head- prev0-1-2-3- prev0- curr1-2-3-
# head0- prev1-2-3- prev1-0- curr2-3-
# head1-0- prev2-3- prev2-1-0- curr3-
# head2-1-0- prev3- prev3-2-1-0- curr-
        