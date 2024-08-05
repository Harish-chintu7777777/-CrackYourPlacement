

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = defaultdict(list)
        indeg = [0] * n
        res = []

        n = len(graph)
        for i in range(n):
            for x in graph[i]:
                adj[x].append(i)
                indeg[i] += 1
        q = []
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        topo = []
        while(q):
            node = q.pop(0)
            topo.append(node)
            for x in adj[node]:
                indeg[x] -= 1
                if indeg[x] == 0:
                    topo.append(x)
        return sorted(topo)
