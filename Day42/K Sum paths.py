#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    

    def sumK(self,root,k):
       
        def f(root, k, count,path):
            if not root:
                return
            path.append(root.data)
            f(root.left,k, count,path)
            f(root.right,k, count,path)
            
            s = 0
            for i in range(len(path) - 1, -1, -1):
                s += path[i]
                if s == k:
                    count[0] += 1
            path.pop()
                
        count = [0]
        path = []
        f(root,k,count,path)
        return count[0]%1000000007
