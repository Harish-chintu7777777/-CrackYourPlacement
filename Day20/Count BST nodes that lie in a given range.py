#User function Template for python3


#Function to count number of nodes in BST that lie in the given range.
class Solution:
    def getCount(self,root,l,h):
        ##Your code here
        c=0
        def inorder(root,l,h):
            nonlocal c
            if not root:return
            
            if l<=root.data<=h:
                c+=1
            inorder(root.left,l,h)
            inorder(root.right,l,h)
        inorder(root,l,h)
        return c
