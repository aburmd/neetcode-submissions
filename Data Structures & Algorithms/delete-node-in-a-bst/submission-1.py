# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNodeVal(self,root):
        if not root:
            return None
        while root and root.left:
            root=root.left
        return root.val
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        else:
            if not root.right and not root.left:
                return None
            elif not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                finMinval=self.findMinNodeVal(root.right)
                root.val=finMinval
                root.right=self.deleteNode(root.right,finMinval)
        return root

        