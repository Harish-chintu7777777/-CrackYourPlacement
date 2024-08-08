from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def bfs(src, tar):
            if src == tar and src in adj and tar in adj:
                return 1.0
            if src not in adj or tar not in adj:
                return -1.0
            
            q = deque([(src, 1.0)])
            vis = set()
            vis.add(src)
            
            while q:
                node, weight = q.popleft()
                
                if node == tar:
                    return weight
                
                for nei, w in adj[node]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append((nei, weight * w))
            
            return -1.0
        
        adj = defaultdict(list)
        for (u, v), value in zip(equations, values):
            adj[u].append((v, value))
            adj[v].append((u, 1 / value))
        
        return [bfs(src, tar) for src, tar in queries]

