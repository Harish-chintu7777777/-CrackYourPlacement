#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        def dfs(node,adj,vis,res):
            vis[node]=1
            res.append(node)
            for i in adj[node]:
                if not vis[i]:
                    dfs(i,adj,vis,res)
        
        
        vis=[0]*V
        start=0
        res=[]
        dfs(start,adj,vis,res)
        return res
