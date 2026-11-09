# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNodeVal(self,root):
        if not root:
            return None
        while root and root.left:
            root=root.left
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < key:
            root.right=self.deleteNode(root.right,key)
        elif root.val > key:
            root.left=self.deleteNode(root.left,key)
        else:
            if not root.left and not root.right:
                del root
                return None
            elif not root.left:
                tmpNode=root.right
                del root
                return tmpNode
            elif not root.right:
                tmpNode=root.left
                del root
                return tmpNode  
            else:
                minVal=self.minNodeVal(root.right)
                root.val=minVal
                root.right=self.deleteNode(root.right,minVal)
        return root