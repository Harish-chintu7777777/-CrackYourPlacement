
class Solution(object):
    def diameterOfBinaryTree(self, root):
        
        def f(root):
            
            if not root:
                return 0
            l = f(root.left)
            r = f(root.right)
            maxi[0] = max(maxi[0],l+r+1)

            return max(l,r) + 1
        maxi = [0]
        f(root)
        return maxi[0] - 1
        
