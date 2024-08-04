class Solution:
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        color = {}
        parent = {}

        for node in range(V):
            color[node] = "W"
            parent[node] = None

        def dfs(u, color, parent):
            color[u] = 'G'

            for v in adj[u]:
                if color[v] == "W":
                    if dfs(v, color, parent):
                        return True
                elif color[v] == "G":
                    return True

            color[u] = "B"
            return False

        for u in range(V):
            if color[u] == "W":
                if dfs(u, color, parent):
                    return True

        return False
