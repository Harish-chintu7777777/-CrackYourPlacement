class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
     
        def f(root):
            if not root:
                return 0
            l = f(root.left)
            r = f(root.right)

            s = max(l,0) + max(r,0) + root.val
            maxi[0] = max(maxi[0],s)
            return max(l,r,0) + root.val

        maxi = [float('-inf')]
        f(root)
        return maxi[0]
