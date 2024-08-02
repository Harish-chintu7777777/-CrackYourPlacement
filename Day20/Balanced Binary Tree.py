# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def f(root):
            nonlocal ans
            if not root:
                return 0

            l = f(root.left)
            r = f(root.right)

            if abs(l-r) > 1:
                ans = False
            
            return 1 + max(l,r)
        ans = True
        if not root:
            return True
        f(root)
        return ans
