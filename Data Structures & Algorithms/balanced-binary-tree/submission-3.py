# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root,height,isBalanced):
        if not root:
            return 0,True
        lheight,l_isBalanced=self.dfs(root.left,height,isBalanced)
        rheight,r_isBalanced=self.dfs(root.right,height,isBalanced)
        if not l_isBalanced or not r_isBalanced or abs(lheight-rheight)>1:
            r_isBalanced=False
        return 1 + max(lheight,rheight), r_isBalanced
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        j,k=self.dfs(root,0,True)
        return k