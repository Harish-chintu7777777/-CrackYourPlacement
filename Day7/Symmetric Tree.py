
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def f(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return f(p.left,q.right) and f(p.right,q.left)

        return f(root,root)
                
