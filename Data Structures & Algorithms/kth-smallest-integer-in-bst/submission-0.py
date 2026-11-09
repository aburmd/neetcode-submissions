# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.srtArr=[]
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        self.srtArr.append(root.val)
        self.inorder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root)
        return self.srtArr[k-1]
        