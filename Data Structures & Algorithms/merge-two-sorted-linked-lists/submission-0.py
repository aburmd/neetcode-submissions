# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        head=ListNode()
        tail=head
        left,right=list1,list2
        while left or right:
            if not left:
                tail.next=right
                break
            elif not right:
                tail.next=left
                break
            if left.val > right.val:
                tail.next=right
                right=right.next
            else:
                tail.next=left
                left=left.next
            tail=tail.next
        return head.next
        



        