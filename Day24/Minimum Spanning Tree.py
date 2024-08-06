class DSU:
    def __init__(self, n):
        self.rank = [1]*n
        self.parent = [i for i in range(n)]

    def find_upar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_upar(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        ulp_u, ulp_v = self.find_upar(u), self.find_upar(v)
        if ulp_u == ulp_v:
            return
        elif self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_u] = ulp_v
            self.rank[ulp_v] += 1

    def size(self, node):
        return self.rank[node]

class Solution:
    def spanningTree(self, V, adj):
        q = []
        dsu = DSU(V)
        
        for i in range(V):
            for (v, wt) in adj[i]:
                q.append((wt, i, v))
        
        q.sort()
        cnt = 0
        
        for wt, i, j in q:
            if dsu.find_upar(i) != dsu.find_upar(j):
                cnt += wt
                dsu.union(i, j)
        
        return cnt
