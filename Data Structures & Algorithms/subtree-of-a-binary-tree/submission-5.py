# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self,p,q):
        if (not p and q) or (not q and p) or (p and q and p.val!=q.val):
            return False
        elif not p and not q:
            return True
        else:
            return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)
       
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.sameTree(root,subRoot):
            return True
        elif root.left and subRoot:
            return self.isSubtree(root.left,subRoot)
        elif root.right and subRoot:
            return self.isSubtree(root.right,subRoot)
        else:
            return False

        