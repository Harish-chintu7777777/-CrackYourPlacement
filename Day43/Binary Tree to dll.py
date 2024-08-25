class Solution:
    def bToDLL(self,root):
        # do Code here
        def dfs(root):
            nonlocal head,prev
            if not root: 
                return
            dfs(root.left)
            if prev==None:
                head=root
                
                
            else:
                root.left=prev
                prev.right=root
            prev=root
            dfs(root.right)
        dfs(root)
        return head
