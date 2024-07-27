from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here


        q=[]
        vis=[0]*V
        for i in range(V):
            if not vis[i]:
                vis[i]=-1
                q.append(i)
                while(q):
                    vtx=q.pop(0)
                    for j in adj[vtx]:
                        if not vis[j]:
                            q.append(j)
                            vis[j]=vtx
                        elif vis[j] and vis[vtx]!=j:
                            return 1
        return 0
