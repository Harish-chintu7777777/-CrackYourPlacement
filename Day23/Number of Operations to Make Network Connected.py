class Union:
    def __init__(self, n):
        self.rank = [0] * (n+1)
        self.parent = [i for i in range(0, n+1)]

    def find_uparent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_uparent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        ulp_u = self.find_uparent(u)
        ulp_v = self.find_uparent(v)

        if ulp_u == ulp_v:
            return

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

class Solution:
    
    def makeConnected(self, n: int, conn: List[List[int]]) -> int:
        ds=Union(n)
        extras=0
        for u,v in conn:
            if ds.find_uparent(u)==ds.find_uparent(v):
                extras+=1
            else:
                ds.union_by_rank(u,v)
        
        cnt=0
        for i in range(n):
            if i==ds.parent[i]:
                cnt+=1

        ans=cnt-1
        if extras>=ans:
            return ans
        return -1
