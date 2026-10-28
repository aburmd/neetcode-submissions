# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        tail=head
        left,right=list1,list2
        while left and right:
            if left.val > right.val:
                tail.next=right
                right=right.next
            else:
                tail.next=left
                left=left.next
            tail=tail.next
        tail.next=left or right
        return head.next
        



        