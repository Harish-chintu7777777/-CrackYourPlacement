# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def f(root,curr):
            if not root.left and not root.right:
                curr += str(root.val)
                l.append(curr)
            if root.left:
                f(root.left,curr + str(root.val) + "->" )
            if root.right:
                f(root.right, curr + str(root.val) + "->")
        l = []
        f(root,"")
        return l
