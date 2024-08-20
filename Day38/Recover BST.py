# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        

        prev = None
        first, second = None, None
        def inorder(x):
            nonlocal prev, first, second
            if not x:
                return
            inorder(x.left)
            if prev and prev.val > x.val:
                if not first:
                    first, second = prev, x
                else:
                    second = x
            prev = x
            inorder(x.right)
        inorder(root)
        first.val, second.val = second.val, first.val
        return root


        
