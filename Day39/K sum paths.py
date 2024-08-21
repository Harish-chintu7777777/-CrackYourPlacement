class Solution:
    
    def solve(self,root,k,count,path):
        if root==None:
            return
        path.append(root.data)
        self.solve(root.left,k,count,path)
        self.solve(root.right,k,count,path)
        s = 0
        for i in range(len(path)-1,-1,-1):
            s+=path[i]
            if s==k:
                count[0]+=1
        path.pop()
    def sumK(self,root,k):
       # code here
        count = [0]
        path = []
        self.solve(root,k,count,path)
        return count[0]%1000000007
        return c
        
        
        
