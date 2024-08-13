

class DSU:
    def __init__(self, N):
        self.rank = [1] * N
        self.size = [1] * N
        self.parent = list(range(N))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unionOf(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
                self.size[py] += self.size[px]
            elif self.rank[py] < self.rank[px]:
                self.parent[py] = px
                self.size[px] += self.size[py]
            else:
                self.parent[px] = py
                self.size[py] += self.size[px]
                self.rank[py] += 1
            return 1
        return 0

    def getSize(self, x):
        return self.size[x]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dsu = DSU(m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for r,c in [[-1,0],[1,0],[0,1],[0,-1]]:
                        nr,nc = r + i, c + j
                        if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                            node = n*nr + nc
                            dsu.unionOf(n*i+j, node)

        
        ans = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dsu.getSize(dsu.find(n * i + j)))
                else:
                    ust = set()
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y]:
                            ust.add(dsu.find(n * x + y))
                    
                    size = 1
                    for a in ust:
                        size += dsu.getSize(dsu.find(a))
                    ans = max(ans, size)
        
        return ans
        
        
