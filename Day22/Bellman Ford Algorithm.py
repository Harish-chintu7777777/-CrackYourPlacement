#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        dist=[1e8]*V
        dist[S]=0
        for i in range(V-1):
            for it in edges:
                u=it[0]
                v=it[1]
                wt=it[2]
                if dist[u]!=1e8 and dist[u]+wt<dist[v]:
                    dist[v]=dist[u]+wt
        
        for i in edges:
            u,v,wt=i[0],i[1],i[2]
            if dist[u]!=1e8 and dist[u]+wt<dist[v]:
                return [-1]
            
        dist=[int(i) for i in dist]
        return dist
