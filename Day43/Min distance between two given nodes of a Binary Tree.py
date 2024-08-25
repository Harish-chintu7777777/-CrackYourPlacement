#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
#     def findDist(self,root,a,b):
    
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

    
    
    def findDist(self,root, a, b):
        def solve(root, a, b, parent, vis, dist):
            if root is None:
                dist[0] = 0
                return dist[0]
        
            if root.data == b:
                return dist[0]
        
            vis[root] = 1
        
            if root.left and not vis.get(root.left):
                l = solve(root.left, a, b, parent, vis, [dist[0] + 1])
                if l:
                    return l
        
            if root.right and not vis.get(root.right):
                r = solve(root.right, a, b, parent, vis, [dist[0] + 1])
                if r:
                    return r
        
            if parent.get(root) and not vis.get(parent[root]):
                p = solve(parent[root], a, b, parent, vis, [dist[0] + 1])
                if p:
                    return p
        r = None
        parent = {}
        q = []
        q.append(root)
    
        while q:
            curr = q.pop(0)
            if curr.data == a:
                r = curr
    
            if curr.left:
                parent[curr.left] = curr
                q.append(curr.left)
    
            if curr.right:
                parent[curr.right] = curr
                q.append(curr.right)
    
        vis = {}
        ans = solve(r, a, b, parent, vis, [0])
        return ans
    

            
                
