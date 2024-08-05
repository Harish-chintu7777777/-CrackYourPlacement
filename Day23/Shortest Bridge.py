Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

class DSU:
    def __init__(self, n: int):
        self.rank = [1] * n
        self.parent = list(range(n))
        
    def find_upar(self, node: int) -> int:
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_upar(self.parent[node])
        return self.parent[node]
    
    def union(self, x: int, y: int) -> None:
        upar_x = self.find_upar(x)
        upar_y = self.find_upar(y)
        
        if upar_x == upar_y:
            return
        
        if self.rank[upar_x] > self.rank[upar_y]:
            self.parent[upar_y] = upar_x
        elif self.rank[upar_x] < self.rank[upar_y]:
            self.parent[upar_x] = upar_y
        else:
            self.parent[upar_y] = upar_x
            self.rank[upar_x] += 1

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dsu = DSU(m * n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nrow, ncol = i + x, j + y
                        if 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] == 1:
                            node, new_node = i * n + j, nrow * n + ncol
                            dsu.union(node, new_node)

...         island_roots = set()
...         for i in range(m):
...             for j in range(n):
...                 if grid[i][j] == 1:
...                     root = dsu.find_upar(i * n + j)
...                     island_roots.add(root)
... 
...         if len(island_roots) != 2:
...             return -1  
... 
...         island_roots = list(island_roots)
...         island1, island2 = [], []
... 
...         for i in range(m):
...             for j in range(n):
...                 node = i * n + j
...                 root = dsu.find_upar(node)
...                 if root == island_roots[0]:
...                     island1.append((i, j))
...                 elif root == island_roots[1]:
...                     island2.append((i, j))
...         queue = deque(island1)
...         visited = set(island1)
...         steps = 0
... 
...         while queue:
...             for _ in range(len(queue)):
...                 x, y = queue.popleft()
...                 for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
...                     nx, ny = x + dx, y + dy
...                     if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
...                         if (nx, ny) in island2:
...                             return steps
...                         if grid[nx][ny] == 0:
...                             queue.append((nx, ny))
...                             visited.add((nx, ny))
...             steps += 1
... 
...         return -1
