#User function Template for python3
from collections import defaultdict
class Solution:

    def kosaraju(self, n, adj):
        # code here
        def dfs(node,st,vis):
            vis[node] = 1
            for it in adj[node]:
                if vis[it] == 0:
                    dfs(it,st, vis)
            st.append(node)
            
        def f(node,vis):
            vis[node] = 1
            for it in rev[node]:
                if vis[it] == 0:
                    f(it,vis)
                
        vis = [0]*n
        st = []
        for i in range(n):
            if vis[i] == 0:
                dfs(i, st, vis)
        rev = [[] for _ in range(n)]
        for i in range(n):
            for k in adj[i]:
                rev[k].append(i)
                
        vis = [0]*n
        cnt = 0
        while(st):
            i = st.pop()
            if vis[i] == 0:
                cnt += 1
                f(i,vis)
        return cnt
            
