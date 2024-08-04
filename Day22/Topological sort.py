class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indeg=[0]*V
        for i in range(V):
            for it in adj[i]:
                indeg[it]+=1
                
                
        q=[]
        for i in range(V):
            if indeg[i]==0:
                q.append(i)
        topo=[]
        while(q):
            node=q.pop(0)
                
            topo.append(node)
            for j in adj[node]:
                indeg[j]-=1
                if indeg[j]==0:
                    q.append(j)
        return topo

