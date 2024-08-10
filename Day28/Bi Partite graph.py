class Solution:
    def isBipartite(self, V, adj):
        vis = [-1] * V
        
        for i in range(V):
            if vis[i] == -1:
                q = [i]
                vis[i] = 1
                
                while q:
                    node = q.pop(0)
                    for neighbor in adj[node]:
                        if vis[neighbor] == -1:
                            vis[neighbor] = 1 - vis[node]
                            q.append(neighbor)
                        elif vis[neighbor] == vis[node]:
                            return 0
        return 1
