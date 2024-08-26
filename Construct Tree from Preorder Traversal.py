def constructTree(pre, preLN, n):
    def solve(pre, preLN, n):

        if len(pre)==0:
    
            return None
    
        root=Node(pre.pop(0))
    
        inst=preLN.pop(0)
    
        if inst=="L":
    
            return root
    
        else:
    
            root.left=constructTree(pre,preLN,n-1)
    
            root.right=constructTree(pre,preLN,n-1)
    
        return root

    return solve(pre, preLN, n)
