class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    
        def dfs(node,par,tin,tlow,bridges,timer):
            vis[node]=1
            tin[node] = tlow[node] = timer
            timer+=1
            for it in adj[node]:
                if par==it:
                    continue
                if vis[it]==0:
                    dfs(it,node,tin,tlow,bridges,timer)
                    tlow[node] = min(tlow[node],tlow[it])
                    if tlow[it]>tin[node]:
                        bridges.append([it,node])
                else:
                    tlow[node] = min(tlow[node],tin[it])


        adj = defaultdict(list)
        for i,j in connections:
            adj[i].append(j)
            adj[j].append(i)
        tlow = [-1]*n
        tin = [-1]*n
        vis = [0]*(n)
        timer = 1
        bridges = []
        dfs(0,-1,tin,tlow,bridges,timer)
        return bridges
