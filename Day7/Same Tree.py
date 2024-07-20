
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def f(p,q):

            if not p and not q:
                return True
            if (p and not q) or (not p and q):
                return False
            if p.val != q.val:
                return False
            
            return f(p.left,q.left) and f(p.right,q.right)
        return f(p,q)
        
    
