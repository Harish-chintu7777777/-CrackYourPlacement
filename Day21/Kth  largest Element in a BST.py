# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        
        def inorder(root, res):
            if root is not None:
                
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)
                
        
        inorder(root, res)
       
        if not res:
            return []
        return res[k-1]
