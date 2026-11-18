# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self,root,height):
        if not root:
            return 0
        ldepth,rdepth=0,0
        if root.left:
            ldepth=self.depth(root.left,1+height)
        if root.right:
            rdepth=self.depth(root.right,1+height)
        return 1+max(ldepth,rdepth)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root,0)

            
        