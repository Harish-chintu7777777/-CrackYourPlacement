class Solution:
    def restoreArray(self, edges: List[List[int]]) -> List[int]:
        def dfs(node,st,vis):
            st.append(node)
            vis.add(node)
            for it in adj[node]:
                if it not in vis:
                    return dfs(it,st,vis)
            return st

        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        v = -1
        for i in adj:
            if len(adj[i]) == 1:
                v = i
                break
        st = []
        vis = set()
        return dfs(v,st,vis)
        
