# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def inorder(self,root):
        if not root:
            return None
        root.left=self.inorder(root.left)
        self.res.append(root.val)
        root.right=self.inorder(root.right)
        return root
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.inorder(root)
        return self.res
        

